clc;clear
%% ��������
m=1765; %��������kg
mb=1600; %��������kg
mw=(m-mb)/4; %��̥����kg
Bf=1.6; %ǰ���־�m
Br=1.6; %�����־�m 1.55
Lf=1.2; %���ľ���ǰ��ľ���m 
Lr=1.4; %���ľ������ľ���m
L=Lf+Lr; %���m 
hg=0.5; %���ľ������߶�m
Iz=2700; %����z��ת������kg*m^2
I_tire=2.5; %��̥ת������/ kg*m^2
f=0.015; %��������ϵ��
r=0.354; %���ֹ����뾶/ m
i_sw=20; %ת��ϵ������
g=9.8; %�������ٶ�
Pn_motor=80; %�������� Kw
Tn_motor=1000; %������Ť�� N*m

vx0=16; %��ʼVx�ٶ� m/s
w0=vx0/r; %��ʼ���� rad/s
v_obj=16; %�������� m/s
u_fl=0.3; %��ǰ�ָ���ϵ��
u_fr=0.8; %��ǰ�ָ���ϵ��
u_rl=0.3; %����ָ���ϵ��
u_rr=0.8; %�Һ��ָ���ϵ��



