#!/usr/bin/env python
# coding=utf-8

import rospy
import math
from std_msgs.msg import String, Int32, Float32, Float64MultiArray

CAR_M = 1412  # 预定以的参数，车辆的固定参数可方这里,注意不要重名
# 设置固有参数,长度参数单位为m，角度为弧度制
lf = 1.015  # 质心到前轮轴的距离
lr = 1.895  # 质心到后轮轴的距离
Bf = Br = 1.675  # 前后轮的距离
R = 0.325  # 轮胎滚动半径
mw = 35.5  # 轮胎质量
ms = 1270  # 簧上质量
hg = 0.5  # 质心到地面的距离
g = 9.8  # 重力加速度
m = mw + ms  # 整车质量
Iz = 1536.7  # 绕z轴旋转的转动惯量
X = 0.6  # 路面附着系数初值
P = 0.001  # 协方差的初值


def callback(This):  # 回调函数，每次话题有更新会执行此函数
    # This.data[0]: delta 左前轮转角, This.data[1]: ax, This.data[2]: ay, This.data[3]: dwz 绕z轴角加速度, This.data[4]: wz 绕z轴角速度,
    # This.data[5]: Vx, This.data[6]: Vy This.data[7]: V_fl, This.data[8]: V_fr, This.data[9]: V_rl,
    # This.data[10]:V_rr 车轮转动角速度, This.data[11]: deltar  右前轮转角
    rospy.loginfo("I heard %s \n", This.data)  # 终端打印
    rospy.loginfo("I heard %s \n", This.data[0])  # 终端打印

    req(This.data[5], This.data[6], This.data[3], This.data[1], This.data[2], This.data[4], This.data[0], This.data[11],
        This.data[7], This.data[8], This.data[9],
        This.data[10])  # reg(vx, vy, wz, ax, ay, dwz, deta, detar, omega_fl, omega_fr, omega_rl, omega_rr):
    ####
    # 你的辨识算法
    ####
    pub.publish(X)


def alpha(delta_l, vx, vy, wz):  # 用于计算车轮侧偏角
    alpha_fl = -delta_l + np.atan((vy + lf * wz) / (vx - Bf * wz / 2))
    alpha_fr = -delta_l + np.atan((vy + lf * wz) / (vx + Bf * wz / 2))
    alpha_rl = np.atan((vy - lr * wz) / (vx - Br * wz / 2))
    alpha_rr = np.atan((vy - lr * wz) / (vx + Br * wz / 2))
    return alpha_fl, alpha_fr, alpha_rl, alpha_rr


def vc(delta_l, vx, vy, wz):  # 用于计算车轮轮心速度
    vc_fl = (vx - Bf * wz / 2) * np.cos(delta_l) + (vy + lf * wz) * np.sin(delta_l)
    vc_fr = (vx + Bf * wz / 2) * np.cos(delta_l) + (vy + lf * wz) * np.sin(delta_l)
    vc_rl = (vx - Br * wz / 2)
    vc_rr = (vx + Br * wz / 2)
    return vc_fl, vc_fr, vc_rl, vc_rr


def lamda(vc_fl, vc_fr, vc_rl, vc_rr, omega_fl, omega_fr, omega_rl, omega_rr):  # 用于计算滑移率
    lamda_fl = (omega_fl * R - vc_fl) / vc_fl
    lamda_fr = (omega_fr * R - vc_fr) / vc_fr
    lamda_rl = (omega_rl * R - vc_rl) / vc_rl
    lamda_rr = (omega_rr * R - vc_rr) / vc_rr
    return lamda_fl, lamda_fr, lamda_rl, lamda_rr


def cfz(ax, ay):  # 用于计算轮胎垂向力 cfz calculate Fz
    cfz_fl = mw * g + ms * g * lr / 2 / (lf + lr) - ms * hg * ax / 2 / (lf + lr) - ms * hg * ay / 2 / Bf
    cfz_fr = mw * g + ms * g * lr / 2 / (lf + lr) - ms * hg * ax / 2 / (lf + lr) + ms * hg * ay / 2 / Bf
    cfz_rl = mw * g + ms * g * lf / 2 / (lf + lr) - ms * hg * ax / 2 / (lf + lr) - ms * hg * ay / 2 / Bf
    cfz_rr = mw * g + ms * g * lf / 2 / (lf + lr) - ms * hg * ax / 2 / (lf + lr) + ms * hg * ay / 2 / Bf
    return cfz_fl, cfz_fr, cfz_rl, cfz_rr


def dg_tire(cfz0, alpha0, lamda0):  # dugoff轮胎模型计算归一化力
    lamda0 = -lamda0
    cx = -30
    cy = -18
    l0 = (1 - lamda0) / (2 * np.sqrt((cx ^ 2) * (lamda0 ^ 2) + (cy ^ 2) * (np.tan(alpha0)) ^ 2))
    if l0 < 1:
        f = l0 * (2 - l0)
    else:
        f = 1
    fx = cfz0 * cx * lamda0 * f / (1 - lamda0)
    fy = cfz0 * cy * np.tan(alpha0) * f / (1 - lamda0)
    return fx, fy


def kalman(Fxfl, Fxfr, Fxrl, Fxrr, Fyfl, Fyfr, Fyrl, Fyrr, ax, ay, dwz, deta,
           detar):  # Fxfl,Fxfr,Fxrl,Fxrr,Fyfl,Fyfr,Fyrl,Fyrr,ax,ay,dwz,deta,detar
    Q = 0.001
    R = np.eye(4) * 50  # 生成4阶对角阵
    global X
    global P
    Xpre = X
    H = np.array([(Fxfl * np.cos(deta) - Fyfl * np.sin(deta)) / m + (
            Fxfr * np.cos(detar) - Fyfr * np.sin(detar)) / m + Fxrl / m + Fxrr / m],
                 [(Fxfl * np.sin(deta) + Fyfl * np.cos(deta)) / m + (
                         Fxfr * np.sin(detar) + Fyfr * np.cos(deta)) / m + Fyrl / m + Fyrr / m],
                 [(lf * (Fxfl * np.sin(deta) + Fyfl * np.cos(deta)) - Bf / 2 * (
                         Fxfl * np.cos(deta) - Fyfl * np.sin(deta))) / Iz + (
                          lf * (Fxfr * np.sin(detar) + Fyfr * np.cos(detar)) + Bf / 2 * (
                          Fxfr * np.cos(detar) - Fyfr * np.sin(detar))) / Iz + (
                          -Br / 2 * Fxrl - lr * Fyrl) / Iz + (Br / 2 * Fxrr - lr * Fyrr) / Iz])
    zjian = H @ Xpre
    PP = P + Q
    if (H @ PP @ H.transpose()) != np.zeros(3, 3):
        Kk = PP @ H.transpose() / (H @ PP @ H.transpose() + R)
        X = Xpre + Kk @ (np.array([ax, ay, dwz]).transpose() - zjian)
        P = PP - Kk @ H @ PP
    else:
        X = np.zeros(1, 1)


def reg(vx, vy, wz, ax, ay, dwz, deta, detar, omega_fl, omega_fr, omega_rl, omega_rr):
    alpha_fl, alpha_fr, alpha_rl, alpha_rr = alpha(deta, vx, vy, wz)
    vc_fl, vc_fr, vc_rl, vc_rr = vc(deta, vx, vy, wz)
    lamda_fl, lamda_fr, lamda_rl, lamda_rr = lamda(vc_fl, vc_fr, vc_rl, vc_rr, omega_fl, omega_fr, omega_rl, omega_rr)
    cfz_fl, cfz_fr, cfz_rl, cfz_rr = cfz(ax, ay)
    fx_fl, fy_fl = dg_tire(cfz_fl, alpha_fl, lamda_fl)
    fx_fr, fy_fr = dg_tire(cfz_fr, alpha_fr, lamda_fr)
    fx_rl, fy_rl = dg_tire(cfz_rl, alpha_rl, lamda_rl)
    fx_rr, fy_rr = dg_tire(cfz_rr, alpha_rr, lamda_rr)
    kalman(fx_fl, fx_fr, fx_rl, fx_rr, fy_fl, fy_fr, fy_rl, fy_rr, ax, ay, dwz, deta, detar)


if __name__ == '__main__':
    rospy.init_node('Recognize', anonymous=True)  # 定义节点
    rospy.Subscriber('/chatter/array0', Float64MultiArray, callback)  # 定义接受接口，包括话题名、数据类型、回调函数
    pub = rospy.Publisher("/chatter/mu", Float32, queue_size=10)
    rospy.spin()
