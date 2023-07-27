


from functools import total_ordering


cake_1 = "Black Forest"
cake_2 = "Red Velvet"
cake_3 = "Vanilla Cake"
cake_4 = "Lemon Sponse Cake"
cake_5 = "Chocolate Cake"

#row matrtial cost each cake inventory = r_m_c

cake_r_m_c_1 = 180
cake_r_m_c_2 = 150
cake_r_m_c_3 = 220
cake_r_m_c_4 = 165
cake_r_m_c_5 = 170


#transportation const =t_c

t_c = 150

#total material cost and transportation cost
cake_r_m_c_t_c_1 = cake_r_m_c_1 + t_c 
cake_r_m_c_t_c_2 = cake_r_m_c_2 + t_c
cake_r_m_c_t_c_3 = cake_r_m_c_3 + t_c
cake_r_m_c_t_c_4 = cake_r_m_c_4 + t_c
cake_r_m_c_t_c_5 = cake_r_m_c_5 + t_c

#utility cost = u_c
cake_u_c_1 = ( cake_r_m_c_t_c_1 * 3 ) /100 
cake_u_c_2 = ( cake_r_m_c_t_c_2 * 3 ) /100
cake_u_c_3 = ( cake_r_m_c_t_c_3 * 3 ) /100
cake_u_c_4 = ( cake_r_m_c_t_c_4 * 3 ) /100
cake_u_c_5 = ( cake_r_m_c_t_c_5 * 3 ) /100

#space cost and staff cost =s_c
s_c = 50
staff_c = 60

total_i_c_1 = (cake_r_m_c_t_c_1 + cake_u_c_1 + s_c + staff_c) * 5
total_i_c_2 = (cake_r_m_c_t_c_2 + cake_u_c_2 + s_c + staff_c) * 7
total_i_c_3 = (cake_r_m_c_t_c_3 + cake_u_c_3 + s_c + staff_c) * 10
total_i_c_4 = (cake_r_m_c_t_c_4 + cake_u_c_4 + s_c + staff_c) * 5
total_i_c_5 = (cake_r_m_c_t_c_5 + cake_u_c_5 + s_c + staff_c) * 9

# 3. cake celling price = s_p
cake_s_p_1 = 780
cake_s_p_2 = 600
cake_s_p_3 = 800
cake_s_p_4 = 650
cake_s_p_5 = 660

# 4. cake celling price after discount 5% = a_dis
cake_s_p_a_dis_1 = (cake_s_p_1 * 5) /100
cake_s_p_a_dis_2 = (cake_s_p_2 * 5) /100
cake_s_p_a_dis_3 = (cake_s_p_3 * 5) /100

cake_s_p_a_dis_4 = (cake_s_p_4 * 7) /100
cake_s_p_a_dis_5 = (cake_s_p_5 * 7) /100

# 4. cake celling price after discount , per cake price
cake_s_p_a_dis_1 = (cake_s_p_1-(cake_s_p_1 * 5) /100) * 5
cake_s_p_a_dis_2 = (cake_s_p_2-(cake_s_p_1 * 5) /100) * 7
cake_s_p_a_dis_3 = (cake_s_p_3-(cake_s_p_1 * 5) /100) * 10
cake_s_p_a_dis_4 = (cake_s_p_4-(cake_s_p_1 * 7) /100) * 5
cake_s_p_a_dis_5 = (cake_s_p_5-(cake_s_p_1 * 7) /100) * 9

# 5. total profit cake
total_profit_cake_1 = cake_s_p_a_dis_1-total_i_c_1
total_profit_cake_2 = cake_s_p_a_dis_2-total_i_c_2
total_profit_cake_3 = cake_s_p_a_dis_3-total_i_c_3
total_profit_cake_4 = cake_s_p_a_dis_4-total_i_c_4
total_profit_cake_5 = cake_s_p_a_dis_5-total_i_c_5

#total profit % of cake

profit_rate_1 = (total_i_c_1 * 100) / (total_profit_cake_1)
profit_rate_2 = (total_i_c_2 * 100) / (total_profit_cake_2)
profit_rate_3 = (total_i_c_3 * 100) / (total_profit_cake_3)
profit_rate_4 = (total_i_c_4 * 100) / (total_profit_cake_4)
profit_rate_5 = (total_i_c_5 * 100) / (total_profit_cake_5)


print(profit_rate_1, profit_rate_2, profit_rate_3,profit_rate_4,profit_rate_5)





