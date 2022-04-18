clc;clear
%% 整车参数
m=1765; %整车质量kg
mb=1600; %车身质量kg
mw=(m-mb)/4; %轮胎重力kg
Bf=1.6; %前轴轮距m
Br=1.6; %后轴轮距m 1.55
Lf=1.2; %质心距离前轴的距离m 
Lr=1.4; %质心距离后轴的距离m
L=Lf+Lr; %轴距m 
hg=0.5; %质心距离地面高度m
Iz=2700; %整车z轴转动惯量kg*m^2
I_tire=2.5; %轮胎转动惯量/ kg*m^2
f=0.015; %滚动阻力系数
r=0.354; %车轮滚动半径/ m
i_sw=20; %转向系传动比
g=9.8; %重力加速度
Pn_motor=80; %电机最大功率 Kw
Tn_motor=1000; %电机最大扭矩 N*m

vx0=16; %初始Vx速度 m/s
w0=vx0/r; %初始轮速 rad/s
v_obj=16; %期望车速 m/s
u_fl=0.3; %左前轮附着系数
u_fr=0.8; %右前轮附着系数
u_rl=0.3; %左后轮附着系数
u_rr=0.8; %右后轮附着系数




