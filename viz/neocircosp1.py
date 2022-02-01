import networkx as nx

g = nx.DiGraph()

g.add_edge('Ngo-18', 'Outreach_tours_and_events')
g.add_edge('Ch-02', 'Outreach_tours_and_events')
g.add_edge('Ngo-18', 'Capacity_building_sustainable_agricultural_techniques')
g.add_edge('Ch-02', 'Capacity_building_sustainable_agricultural_techniques')
g.add_edge('Ngo-18', 'Capacity_building_sustainable_management_of_chinampas')
g.add_edge('Ch-07', 'Capacity_building_sustainable_management_of_chinampas')
g.add_edge('Ngo-18', 'Capacity_building_economic_tools_for_projects')
g.add_edge('Ch-10', 'Capacity_building_economic_tools_for_projects')
g.add_edge('Ngo-18', 'Outreach_tours_and_events')
g.add_edge('Ch-10', 'Outreach_tours_and_events')
g.add_edge('Ngo-18', 'Research_water_quality')
g.add_edge('Ac-01', 'Research_water_quality')
g.add_edge('Ngo-18', 'Capacity_building_sustainable_management_of_chinampas')
g.add_edge('Ac-01', 'Capacity_building_sustainable_management_of_chinampas')
g.add_edge('Ngo-18', 'Outreach_chinampas_products_and_social_projects')
g.add_edge('Ac-01', 'Outreach_chinampas_products_and_social_projects')
g.add_edge('Ngo-18', 'Outreach_chinampas_projects')
g.add_edge('Gov-15', 'Outreach_chinampas_projects')
g.add_edge('Ngo-18', 'Project_restoration_and_chinampas_refugees')
g.add_edge('Cs-05', 'Project_restoration_and_chinampas_refugees')
g.add_edge('Cs-05', 'Project_restoration_and_chinampas_refugees')
g.add_edge('Cs-17', 'Project_restoration_and_chinampas_refugees')
g.add_edge('Ngo-18', 'Research_water_quality')
g.add_edge('Ac-19', 'Research_water_quality')
g.add_edge('Ac-19', 'Research_water_quality')
g.add_edge('Ac-01','Research_water_quality')

df = nx.to_pandas_adjacency(g)
df.to_csv('t0.csv')



g = nx.DiGraph()

g.add_edge('Ngo-18', 'Outreach_tours_and_events')
g.add_edge('Ch-02', 'Outreach_tours_and_events')
g.add_edge('Ngo-18', 'Capacity_building_sustainable_agricultural_techniques')
g.add_edge('Ch-02', 'Capacity_building_sustainable_agricultural_techniques')
g.add_edge('Ngo-18', 'Capacity_building_sustainable_management_of_chinampas')
g.add_edge('Ch-07', 'Capacity_building_sustainable_management_of_chinampas')
g.add_edge('Ngo-18', 'Capacity_building_economic_tools_for_projects')
g.add_edge('Ch-10', 'Capacity_building_economic_tools_for_projects')
g.add_edge('Ngo-18', 'Outreach_tours_and_events')
g.add_edge('Ch-10', 'Outreach_tours_and_events')
g.add_edge('Ngo-18', 'Capacity_building_sustainable_management_of_chinampas')
g.add_edge('Ac-01', 'Capacity_building_sustainable_management_of_chinampas')
g.add_edge('Ngo-18', 'Outreach_chinampas_products_and_social_projects')
g.add_edge('Ac-01', 'Outreach_chinampas_products_and_social_projects')
g.add_edge('Ngo-18', 'Outreach_chinampas_projects')
g.add_edge('Gov-15', 'Outreach_chinampas_projects')
g.add_edge('Ngo-18', 'Project_restoration_and_chinampas_refugees')
g.add_edge('Cs-05', 'Project_restoration_and_chinampas_refugees')
g.add_edge('Cs-05', 'Project_restoration_and_chinampas_refugees')
g.add_edge('Cs-17', 'Project_restoration_and_chinampas_refugees')
g.add_edge('Ngo-18', 'Research_water_quality')
g.add_edge('Ac-19', 'Research_water_quality')
g.add_edge('Ngo-18', 'Capacity_building_reforestation')
g.add_edge('Ch-07', 'Capacity_building_reforestation')
g.add_edge('Cs-16', 'Project_rainwater_harvesting_systems')
g.add_edge('Ngo-04', 'Project_rainwater_harvesting_systems')
g.add_edge('Cs-16', 'Alliance_farmers_market_certification')
g.add_edge('Ch-10', 'Alliance_farmers_market_certification')
g.add_edge('Cs-16', 'Alliance_advise_on_irregular_settlements_involvement')
g.add_edge('Ch-14', 'Alliance_advise_on_irregular_settlements_involvement')

df = nx.to_pandas_adjacency(g)
df.to_csv('t1.csv')








