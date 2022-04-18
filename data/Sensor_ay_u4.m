function y =Sensor_ay_u4(x,u)
m=1765; %整车质量kg 
y=(u(2)*sin(u(1))+u(6)*cos(u(1)))*x(1)/m+(u(3)*sin(u(1))+u(7)*cos(u(1)))*x(1)/m+u(8)*x(1)/m+u(9)*x(1)/m;
end