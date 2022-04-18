function [x0,H, ccc]= fcn(Fxfl,Fxfr,Fxrl,Fxrr,Fyfl,Fyfr,Fyrl,Fyrr,ax,ay,dwz,deta,detar)
persistent X P a;
if isempty(X)
    X = ones(4, 1)*0.6;
    P =diag([1,1,1,1])*0.001;
    a=0;
end

m=1765;
la=1.2; %质心距离前轴的距离m 1.27 
lb=1.2; %质心距离后轴的距离m
Tf=1.6; %前轴轮距m
Tr=1.6; %后轴轮距m 1.55
Iz=2700; %整车z轴转动惯量kg*m^2
Q = diag([1,1,1,1])*0.001;
R = diag([1,1,1])*10;
Xpre = X;
%F = diag([1,1,1,1]);
H = [(Fxfl*cos(deta)-Fyfl*sin(deta))/m,(Fxfr*cos(detar)-Fyfr*sin(detar))/m,Fxrl/m,Fxrr/m;(Fxfl*sin(deta)+Fyfl*cos(deta))/m,(Fxfr*sin(detar)+Fyfr*cos(deta))/m,Fyrl/m,Fyrr/m;(la*(Fxfl*sin(deta)+Fyfl*cos(deta))-Tf/2*(Fxfl*cos(deta)-Fyfl*sin(deta)))/Iz,(la*(Fxfr*sin(detar)+Fyfr*cos(detar))+Tf/2*(Fxfr*cos(detar)-Fyfr*sin(detar)))/Iz,(-Tr/2*Fxrl-lb*Fyrl)/Iz,(Tr/2*Fxrr-lb*Fyrr)/Iz];
zjian =H*Xpre; 
PP=P+Q;
a=a+1;
% if a>0
if (H*PP*H')~=zeros(3,3)

% if(det(H*PP*H'+R)==0)
%     X = ones(4, 1);
% else
Kk=PP*H'/(H*PP*H'+R);
X=Xpre+Kk*([ax,ay,dwz]'-zjian);
p=P
P=PP-Kk*H*PP;
% end

if(X(1)>1||X(1)<0||X(2)<0||X(3)<0||X(4)<0||X(2)>1||X(3)>1||X(4)>1)
    X=ones(4, 1)*0.8;
    P=diag([1,1,1,1])*0.001;
else
end
x0=X;
ccc = 0;
else
    x0 = zeros(4,1);
    ccc = 1;
    
end
% else
%     x0 = zeros(4,1);
%     X=ones(4, 1)*0.5;
%     P=diag([1,1,1,1])*0.1;
%     ccc = 2;
% end
end


 