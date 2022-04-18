function y =Sensor_ay_u3(x,u)
m=1765; %整车质量kg 
y=(u(2)*sin(u(1))+u(6)*cos(u(1)))*x/m+(u(3)*sin(u(10))+u(7)*cos(u(10)))*x/m+u(8)*x/m+u(9)*x/m;
end