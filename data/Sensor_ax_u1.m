function y =Sensor_ax_u1(x,u)
m=1765; %整车质量kg
y=(u(2)*cos(u(1))-u(6)*sin(u(1)))*x(1)/m+(u(3)*cos(u(10))-u(7)*sin(u(10)))*x(2)/m+u(4)*x(3)/m+u(5)*x(4)/m; 
end