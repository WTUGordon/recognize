function y =Sensor_ax_u2(x,u)
m=1412; %整车质量kg
a=1.015;
b=1.895;
k1=-70000;
k2=-70000;
y=((a*k1-b*k2)/m/x(3)*x(1)+(k1+k2)/m*x(2)-k1/m*u(1)); 
end