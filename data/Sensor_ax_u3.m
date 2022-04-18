function y =Sensor_ax_u3(x,u)
m=1765; %整车质量kg
y=(u(2)*cos(u(1))-u(6)*sin(u(1)))*x/m+(u(3)*cos(u(10))-u(7)*sin(u(10)))*x/m+u(4)*x/m+u(5)*x/m; 
end