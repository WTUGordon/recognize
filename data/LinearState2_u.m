function x = LinearState2_u(x,u)
dt=0.01; 
a=1.015;
b=1.895;
k1=-70000;
k2=-70000;
m=1412;
Iz=1.536700000000000e+03;
x(1)=((a^2*k1+b^2*k2)/Iz/x(3)*x(1)+(a*k1-b*k2)/Iz*x(2)-a*k1/Iz*u(1))*dt+x(1);
x(2)=(((a*k1-b*k2)/m/x(3)^2-1)*x(1)+(k1+k2)/m/x(3)*x(2)-k1/m/x(3)*u(1))*dt+x(2);
x(3)=(x(1)*x(2)*x(3)+u(2))*dt+x(3);

end
