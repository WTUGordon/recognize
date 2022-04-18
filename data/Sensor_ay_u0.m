function y =Sensor_ay_u0(x,u)
m=1765; %整车质量kg 
y=(u(2)*sin(u(1))+u(6)*cos(u(1)))*x(1)/m+(u(3)*sin(u(10))+u(7)*cos(u(10)))*x(2)/m+(u(4)*sin(u(11))+u(8)*cos(u(11)))*x(3)/m+(u(5)*sin(u(12))+u(9)*cos(u(12)))*x(4)/m;
end