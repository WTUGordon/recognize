function y =Sensor_wz_u3(x,u)
Lf=1.2; %���ľ���ǰ��ľ���m 1.27 
Lr=1.2; %���ľ������ľ���m
Bf=1.6; %ǰ���־�m
Br=1.6; %�����־�m 1.55
Iz=2700; %����z��ת������kg*m^2
y=x*(Lf*(u(2)*sin(u(1))+u(6)*cos(u(1)))-0.5*Bf*(u(2)*cos(u(1))-u(6)*sin(u(1))))/Iz+x*(Lf*(u(3)*sin(u(10))+u(7)*cos(u(10)))+0.5*Bf*(u(3)*cos(u(10))-u(7)*sin(u(10))))/Iz-x*(0.5*Br*u(4)+Lr*u(8))/Iz+x*(0.5*Br*u(5)-Lr*u(9))/Iz;
end