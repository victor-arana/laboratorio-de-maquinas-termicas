def interpolar(f_a, f_b, a, b, c):
    return (((b-c)/(b-a))*(f_a - f_b) + f_b)

# Calculo de entalpias
# Datos conocidos
c_p = 4.186 #[kJ/(kg * K)]
P_atm = 0.796 #[kg/cm^2]
X_1 = 0.96

#Lecturas
P_1m = 5.5 #[kg/cm^2]
P_2m = 3.15 #[kg/cm^2]
P_3m = 20 #[cmHg]
T_3 = 79 #[°C]
T_4 = 61 #[°C]
T_5 = 22 #[°C]

#Conversion de unidades
    # Factores Unitarios
    # 1 kg/cm^2 = 98.07 kPa
    # 1 cmHg = 1.333224 kPa
    # 1 C = 275.15 K
P_atm = P_atm * (98.076/1) # kg/cm^2 --> kPa
P_1m = P_1m * (98.076/1) # kg/cm^2 --> kPa
P_2m = P_2m * (98.076/1) # kg/cm^2 --> kPa    
P_3m = P_3m * (1.333224/1) # cmHg --> kPa
T_5 = T_5 * (275.15/1) #[K]

#Conversion a presiones absolutas
P_1 = P_1m  + P_atm
P_2 = P_2m  + P_atm
P_3 = P_atm - P_3m

 # Para utilizar tablas requiero la presion en kPa
print("Calculo de entalpias:")
print("P_1 (abs) = ", P_1, "[kPa]")
print("P_2 (abs) = ", P_2, "[kPa]")
print("P_3 (abs) = ", P_3, "[kPa]")

# Calculo de entalpias
# Estado 5
h_5 = c_p * (T_5 - 273.15) #[kJ/Kg]
# Estado 1

# Con P_1 = 617.44876 [kPa] 
P_1a = 650 # [kPa] 
P_1b = 700 # [kPa]
h_f1a = 684.08 # [kJ/kg]
h_f1b = 697.00 # [kJ/kg]
h_fg1a = 2075.5 # [kJ/kg]
h_fg1b = 2065.8 # [kJ/kg]

h_f1 = interpolar(h_f1a, h_f1b, P_1a, P_1b, P_1) # [kJ/kg]
h_fg1 = interpolar(h_fg1a, h_fg1b, P_1menor, P_1mayor, P_1) # [kJ/kg]

h_1 = h_f1 + X*h_fg1

h_2 = h1

# Con P_2 = 386.98 [kPa]
P_2a = 650 # [kPa] 
P_2b = 700 # [kPa]
h_f2a = 684.08 # [kJ/kg]
h_f2b = 697.00 # [kJ/kg]
h_fg2a = 2075.5 # [kJ/kg]
h_fg2b = 2065.8 # [kJ/kg]

h_f2 = interpolar(594.73, 604.66, 375, 400,  P_2) # [kJ/kg]
h_fg2 = interpolar(2140.4, 2133.4, 375, 400,  P_2) # [kJ/kg]


print("Estado 1:")
print("X = ", X*100, "%")
print("h_f1@617.4[kPa] =", h_f1, "[kJ/kg]")
print("h_fg1@617.4 [kPa] =", h_fg1, "[kJ/kg]")
print("h_1 = h_f1 + X*h_fg1")
print("h_1 =", h_f1,"[kJ/kg]","+","(",X,")","[1]","(",h_fg1,")","[kJ/kg]")
print("h_1 =", h_1, "[kJ/kg]")


print("Estado 2:")
print("h_1 = h_2")
print("h_2 = ", h_1, "[kJ/kg]")


print("Estado 3")
print("h_3T = h_f3 + X_3*s_fg3")
print("s_3T = s_2 = s_f3 + X_3*s_fg3")
print("X_3 = (s_2 - s_f3)/s_fg3")
print("s_2 = s_f2 + X_2*s_fg2")
print("X_2 = (h_2 - h_f2)/(h_fg2)")
print("Obteniendo h_f2 y h_fg2 de tablas con P_2 =", P_2, "[kPa]")
h_f2 = inter_lin(594.73, 604.66, 375, 400,  P_2) # [kJ/kg]
h_fg2 = inter_lin(2140.4, 2133.4, 375, 400,  P_2) # [kJ/kg]
print("h_f2@386.98[kPa] =", h_f2, "[kJ/kg]")
print("h_fg2@386.98[kPa] =", h_fg2, "[kJ/kg]")
print("Sustituyendo h_f2 y h_fg2")
h_2 = h_1
X_2 = (h_2 - h_f2)/(h_fg2)
print("X_2 = ", X_2)
print("Obteniendo s_f2 y s_fg2 de tablas con P_2 =", P_2, "[kPa]")
s_f2 = inter_lin(1.7526, 1.7765, 375, 400,  P_2) # [kJ/kg K]
s_fg2 = inter_lin(5.1645, 5.1191, 375, 400,  P_2) # [kJ/kg K]
print("s_f2@386.98[kPa] =", s_f2, "[kJ/kg K]")
print("s_fg2@386.98[kPa] =", s_fg2, "[kJ/kg K]")
print("Sustituyendo")
s_2 = s_2 = s_f2 + X_2*s_fg2
print("s_2 =", s_2, "[kJ/kg K]")
print("Obteniendo s_f3 y s_fg3 de tablas con P_3 =", P_3, "[kPa]")
s_f3 = inter_lin(6.5019, 6.2426, 50, 75,  P_3) # [kJ/kg K]
s_fg3 = inter_lin(7.5931, 7.4558, 50, 75,  P_3) # [kJ/kg K]
print("s_f3@51.39[kPa] =", s_f3, "[kJ/kg K]")
print("s_fg3@51.39[kPa] =", s_fg3, "[kJ/kg K]")
print("Sustituyendo s_2, s_f3 y s_fg3")
X_3 = (s_2 - s_f3)/s_fg3
print("X_3 = ", X_3)
print("Obteniendo h_f3 y h_fg3 de tablas con P_3 =", P_3, "[kPa]")
h_f3 = inter_lin(340.54, 384.44, 50, 75,  P_3) # [kJ/kg K]
h_fg3 = inter_lin(2304.7, 2278.0, 50, 75,  P_3) # [kJ/kg K]
print("h_f3@51.39[kPa] =", h_f3, "[kJ/kg]")
print("h_fg3@51.39[kPa] =", h_fg3, "[kJ/kg]")
print("Sustituyendo X_3, h_f3 y h_fg3")
h_3T = h_f3 + X_3*s_fg3
print("h_3T = ", h_3T, "[kJ/kg]")
