"""
Python model "IWRET_7.py"
Translated using PySD version 0.9.0
"""
from __future__ import division
import numpy as np
from pysd import utils
import xarray as xr

from pysd.py_backend.functions import cache
from pysd.py_backend import functions

_subscript_dict = {}

_namespace = {
    u'Result System Acceptability':
    u'result_system_acceptability',
    u'Retail Upper VC':
    u'retail_upper_vc',
    u'SWP Variable Speed Drive Efficiency':
    u'swp_variable_speed_drive_efficiency',
    'Time':
    'time',
    u'WWTW Operation GHG':
    u'wwtw_operation_ghg',
    u'Footprint Office Buildings':
    u'footprint_office_buildings',
    u'SWCS Construction Energy M2':
    u'swcs_construction_energy_m2',
    u'RHP Unit Conversion Factor':
    u'rhp_unit_conversion_factor',
    u'Green Roof Runoff Daily':
    u'green_roof_runoff_daily',
    u'WWTW Space Requirements':
    u'wwtw_space_requirements',
    u'Landuse2 EMC Nitrogen':
    u'landuse2_emc_nitrogen',
    u'SWCS Replacement':
    u'swcs_replacement',
    u'Water Conduit Available Capacity':
    u'water_conduit_available_capacity',
    u'MF Dishwasher Demand':
    u'mf_dishwasher_demand',
    u'RH System Construction GHG':
    u'rh_system_construction_ghg',
    u'SF Other':
    u'sf_other',
    u'RB and Cistern Annual Maintenance Costs':
    u'rb_and_cistern_annual_maintenance_costs',
    u'RHP Average Dynamic Head':
    u'rhp_average_dynamic_head',
    u'WTW Daily Treatment Capacity':
    u'wtw_daily_treatment_capacity',
    u'Community Center Demand Variation Coefficient':
    u'community_center_demand_variation_coefficient',
    u'Bioswale Percentage':
    u'bioswale_percentage',
    u'Result Network Embodied Energy':
    u'result_network_embodied_energy',
    u'WTM Total Costs':
    u'wtm_total_costs',
    u'WDM Running Costs':
    u'wdm_running_costs',
    u'Bioswale Daily Costs':
    u'bioswale_daily_costs',
    u'WDM LC Embodied GHG':
    u'wdm_lc_embodied_ghg',
    u'WWTW Embodied Energy for Chemicals':
    u'wwtw_embodied_energy_for_chemicals',
    u'WWTW Embodied GHG for Chemicals':
    u'wwtw_embodied_ghg_for_chemicals',
    u'WTM Annual Maintenance':
    u'wtm_annual_maintenance',
    u'SWCS Unit Construction Energy M2':
    u'swcs_unit_construction_energy_m2',
    u'SWCS Unit Construction Energy M1':
    u'swcs_unit_construction_energy_m1',
    u'GWP Unit Conversion Factor':
    u'gwp_unit_conversion_factor',
    u'SF Lawn Area':
    u'sf_lawn_area',
    u'GWS Tank Outflow':
    u'gws_tank_outflow',
    u'SF New Units Annually':
    u'sf_new_units_annually',
    u'WTW Daily Maintenance':
    u'wtw_daily_maintenance',
    u'SWTW Total Costs':
    u'swtw_total_costs',
    u'LM Inflow Hospitals':
    u'lm_inflow_hospitals',
    u'MF Clothes Washer Demand':
    u'mf_clothes_washer_demand',
    u'GWP Daily GHG Emissions':
    u'gwp_daily_ghg_emissions',
    u'MBR Total LCC':
    u'mbr_total_lcc',
    u'Green Roof Footprint':
    u'green_roof_footprint',
    u'Landuse4 EMC Nitrogen':
    u'landuse4_emc_nitrogen',
    u'WTW Embodied Energy for Chemicals':
    u'wtw_embodied_energy_for_chemicals',
    u'WTW Affordability':
    u'wtw_affordability',
    u'WDM Construction GHG M2':
    u'wdm_construction_ghg_m2',
    u'WTW Total Sodium Hypochlorite GHG':
    u'wtw_total_sodium_hypochlorite_ghg',
    u'Dem Schools Restrooms':
    u'dem_schools_restrooms',
    u'OB Unit Demand per m2':
    u'ob_unit_demand_per_m2',
    u'PP Footprint':
    u'pp_footprint',
    u'Asphalt Construction Energy':
    u'asphalt_construction_energy',
    u'Public spaces for Irrigation':
    u'public_spaces_for_irrigation',
    u'SF WEC Faucet':
    u'sf_wec_faucet',
    u'Neighborhood Population':
    u'neighborhood_population',
    u'MBR Number of MBR':
    u'mbr_number_of_mbr',
    u'WWTW Total Methanol':
    u'wwtw_total_methanol',
    u'Green Roof LCC':
    u'green_roof_lcc',
    u'Bioretention Risk to Human Health':
    u'bioretention_risk_to_human_health',
    u'Restaurants Lower VC':
    u'restaurants_lower_vc',
    u'SF Leaks':
    u'sf_leaks',
    u'Bioretention Construction GHG':
    u'bioretention_construction_ghg',
    u'WP Risk to Human Health':
    u'wp_risk_to_human_health',
    u'GWP Pump Efficiency':
    u'gwp_pump_efficiency',
    u'Dem Office Buildings':
    u'dem_office_buildings',
    u'WTW Unit Microsand':
    u'wtw_unit_microsand',
    u'Bioswale Space Requirements':
    u'bioswale_space_requirements',
    u'RHP Daily Energy':
    u'rhp_daily_energy',
    u'GWS Reliability':
    u'gws_reliability',
    u'WP Total Dynamic Head of Pump':
    u'wp_total_dynamic_head_of_pump',
    u'WWTW Sludge Generated':
    u'wwtw_sludge_generated',
    u'Asphalt CC Unit Cost':
    u'asphalt_cc_unit_cost',
    u'Restaurants Demand Variation Coefficient':
    u'restaurants_demand_variation_coefficient',
    u'Result Network LCC':
    u'result_network_lcc',
    u'WTW Total Calcium Hydroxide':
    u'wtw_total_calcium_hydroxide',
    u'Green Roof Reliability':
    u'green_roof_reliability',
    u'WWTW Total Ethanol':
    u'wwtw_total_ethanol',
    u'WWCS Unit Construction Energy M2':
    u'wwcs_unit_construction_energy_m2',
    u'WWCS Unit Construction Energy M1':
    u'wwcs_unit_construction_energy_m1',
    u'WTM Daily Maintenance':
    u'wtm_daily_maintenance',
    u'WP Pump Efficiency':
    u'wp_pump_efficiency',
    u'LM kWh per m3':
    u'lm_kwh_per_m3',
    u'Months Counter':
    u'months_counter',
    u'WWP Affordability':
    u'wwp_affordability',
    u'Daycares Demand Variation Coefficient':
    u'daycares_demand_variation_coefficient',
    u'SF WEC Bathtub':
    u'sf_wec_bathtub',
    u'LM Affordability':
    u'lm_affordability',
    u'Dem Hotels':
    u'dem_hotels',
    u'LM Total Energy':
    u'lm_total_energy',
    u'GWP Construction and Installation':
    u'gwp_construction_and_installation',
    u'Result System Reliability':
    u'result_system_reliability',
    u'MBR Total Energy':
    u'mbr_total_energy',
    u'Retail space in m2':
    u'retail_space_in_m2',
    u'WP Duration of Pump Operation':
    u'wp_duration_of_pump_operation',
    u'GWS Space Requirements':
    u'gws_space_requirements',
    u'WWCS Total Costs':
    u'wwcs_total_costs',
    u'RR Total GHG Urea':
    u'rr_total_ghg_urea',
    u'WTW Total Calcium Hydroxide EmEnergy':
    u'wtw_total_calcium_hydroxide_emenergy',
    u'Full Load Water Use':
    u'full_load_water_use',
    u'WWTW Unit Methanol GHG':
    u'wwtw_unit_methanol_ghg',
    u'SWTW Affordability':
    u'swtw_affordability',
    u'LM Total Treated':
    u'lm_total_treated',
    u'WWP CO2 per kWh':
    u'wwp_co2_per_kwh',
    u'WDM Construction':
    u'wdm_construction',
    u'Wastewater Generated':
    u'wastewater_generated',
    u'RH System Total Construction GHG':
    u'rh_system_total_construction_ghg',
    u'WDM Unit Weight M1':
    u'wdm_unit_weight_m1',
    u'WP Affordability':
    u'wp_affordability',
    u'WDM Unit Weight M2':
    u'wdm_unit_weight_m2',
    u'WTW Total Carbon Dioxide EmEnergy':
    u'wtw_total_carbon_dioxide_emenergy',
    u'RB and Cistern Footprint':
    u'rb_and_cistern_footprint',
    u'SF WEC Leaks':
    u'sf_wec_leaks',
    u'WWP Total Dynamic Head':
    u'wwp_total_dynamic_head',
    u'WTW Operation GHG':
    u'wtw_operation_ghg',
    u'SF Initial Stock of Units':
    u'sf_initial_stock_of_units',
    u'Landuse1 EMC Nitrogen':
    u'landuse1_emc_nitrogen',
    u'WWTW Administration Rate':
    u'wwtw_administration_rate',
    u'Result Network Embodied GHG Emissions':
    u'result_network_embodied_ghg_emissions',
    u'SWCS Total Costs':
    u'swcs_total_costs',
    u'GWS Tank Inflow':
    u'gws_tank_inflow',
    u'RR Unit Urea':
    u'rr_unit_urea',
    u'Bioswale Design and Capital Costs':
    u'bioswale_design_and_capital_costs',
    u'Green Roof Construction GHG':
    u'green_roof_construction_ghg',
    u'WTW Unit Sodium Hypochlorite EmEnergy':
    u'wtw_unit_sodium_hypochlorite_emenergy',
    u'WWTW Capital Investment':
    u'wwtw_capital_investment',
    u'LM Flexibility and Adaptability':
    u'lm_flexibility_and_adaptability',
    u'GWP Variable Speed Drive Efficiency':
    u'gwp_variable_speed_drive_efficiency',
    u'WWTW Acceptability':
    u'wwtw_acceptability',
    u'Landuse1 Percentage':
    u'landuse1_percentage',
    u'WDM Construction GHG M1':
    u'wdm_construction_ghg_m1',
    u'LM Acceptability':
    u'lm_acceptability',
    u'SWP Space Requirements':
    u'swp_space_requirements',
    u'Porous Pavement Affordability':
    u'porous_pavement_affordability',
    u'WTW Total Alum EmEnergy':
    u'wtw_total_alum_emenergy',
    u'Dem HVAC':
    u'dem_hvac',
    u'WTW Available Capacity':
    u'wtw_available_capacity',
    u'RR Daily Urea':
    u'rr_daily_urea',
    u'WWCS Unit Construction GHG M1':
    u'wwcs_unit_construction_ghg_m1',
    u'WWCS Unit Construction GHG M2':
    u'wwcs_unit_construction_ghg_m2',
    u'SWTW Average Salary':
    u'swtw_average_salary',
    u'WP Total LCC':
    u'wp_total_lcc',
    u'WWP Unit Conversion Factor':
    u'wwp_unit_conversion_factor',
    u'MF WD per Capita Water Sensitive':
    u'mf_wd_per_capita_water_sensitive',
    u'GWS Daily Maintenance':
    u'gws_daily_maintenance',
    u'WWTW Available Capacity':
    u'wwtw_available_capacity',
    u'RH Tank Inflow':
    u'rh_tank_inflow',
    u'WWTW Flexibility and Adaptability':
    u'wwtw_flexibility_and_adaptability',
    u'PP Daily Costs':
    u'pp_daily_costs',
    u'RR Unit EmEnergy Urea':
    u'rr_unit_emenergy_urea',
    u'SW Daily Rate':
    u'sw_daily_rate',
    u'WWP Space Requirements':
    u'wwp_space_requirements',
    u'WWCS Disposal':
    u'wwcs_disposal',
    u'Rainfall':
    u'rainfall',
    u'SWCS Total Weight M2':
    u'swcs_total_weight_m2',
    u'WTW Water Resource Fee':
    u'wtw_water_resource_fee',
    u'Unit Demand per m2':
    u'unit_demand_per_m2',
    u'SWP Total Energy':
    u'swp_total_energy',
    u'Bioretention Design and Capital Costs':
    u'bioretention_design_and_capital_costs',
    u'Green Roof Design and Capital Costs':
    u'green_roof_design_and_capital_costs',
    u'Irrigation Demand':
    u'irrigation_demand',
    u'WTW Total Carbon Dioxide GHG':
    u'wtw_total_carbon_dioxide_ghg',
    u'SWTW Capital Investment':
    u'swtw_capital_investment',
    u'SWCS Daily Maintenance':
    u'swcs_daily_maintenance',
    u'SWCS Total Weight M1':
    u'swcs_total_weight_m1',
    u'Landuse4 Percentage':
    u'landuse4_percentage',
    u'MBR Affordability':
    u'mbr_affordability',
    u'LM Space Requirements':
    u'lm_space_requirements',
    u'Bioswale LCC':
    u'bioswale_lcc',
    u'Retail Demand Variation Coefficient':
    u'retail_demand_variation_coefficient',
    u'WTW Total Polyaluminium Chloride EmEnergy':
    u'wtw_total_polyaluminium_chloride_emenergy',
    u'SWTW Daily Maintenance':
    u'swtw_daily_maintenance',
    u'Porous Pavement Flexibility and Adaptability':
    u'porous_pavement_flexibility_and_adaptability',
    u'SWP Unit Conversion Factor':
    u'swp_unit_conversion_factor',
    u'SWT Unit Ferric Chloride GHG':
    u'swt_unit_ferric_chloride_ghg',
    u'Result Reached System Capacity':
    u'result_reached_system_capacity',
    u'WWTW Construction and Installation':
    u'wwtw_construction_and_installation',
    u'WWTW Total Ferric Chloride EmEnergy':
    u'wwtw_total_ferric_chloride_emenergy',
    u'SWTW Construction and Installation':
    u'swtw_construction_and_installation',
    u'SWTW Unit Ferric Chloride':
    u'swtw_unit_ferric_chloride',
    u'WSC Construction':
    u'wsc_construction',
    u'WTW Total Calcium Hydroxide GHG':
    u'wtw_total_calcium_hydroxide_ghg',
    u'WWP Daily Costs':
    u'wwp_daily_costs',
    u'SF Stock of Units':
    u'sf_stock_of_units',
    u'Water Supply Leakage Rate':
    u'water_supply_leakage_rate',
    u'LM Daily Treated':
    u'lm_daily_treated',
    u'LM Percentage of OB':
    u'lm_percentage_of_ob',
    u'WWTW Unit Ferric Chloride':
    u'wwtw_unit_ferric_chloride',
    u'TIME STEP':
    u'time_step',
    u'WWTW Daily Treatment Capacity':
    u'wwtw_daily_treatment_capacity',
    u'GWS Total Installation and Construction Costs':
    u'gws_total_installation_and_construction_costs',
    u'Number of Students':
    u'number_of_students',
    u'Result System Total LCC':
    u'result_system_total_lcc',
    u'MF Average Occupancy per Unit':
    u'mf_average_occupancy_per_unit',
    u'WTW Total Costs':
    u'wtw_total_costs',
    u'MBR kWh per m3':
    u'mbr_kwh_per_m3',
    u'Schools Demand Variation Coefficient':
    u'schools_demand_variation_coefficient',
    u'SWT Total Ferric Chloride EmEnergy':
    u'swt_total_ferric_chloride_emenergy',
    u'Bioswale Flexibility and Adaptability':
    u'bioswale_flexibility_and_adaptability',
    u'OB Upper VC':
    u'ob_upper_vc',
    u'Landuse4':
    u'landuse4',
    u'SF Stock of Water Sensitive Units':
    u'sf_stock_of_water_sensitive_units',
    u'Days in a Year':
    u'days_in_a_year',
    u'GWS Affordability':
    u'gws_affordability',
    u'Landuse1':
    u'landuse1',
    u'Landuse2':
    u'landuse2',
    u'SF WEC Clothes Washer':
    u'sf_wec_clothes_washer',
    u'LM Maximum Daily Capacity':
    u'lm_maximum_daily_capacity',
    u'SWP Daily GHG Emissions':
    u'swp_daily_ghg_emissions',
    u'WWTW Unit Nitric Acid GHG':
    u'wwtw_unit_nitric_acid_ghg',
    u'RWH Affordability':
    u'rwh_affordability',
    u'OB Demand Variation Coefficient':
    u'ob_demand_variation_coefficient',
    u'WWTW Sludge Transport and Disposal':
    u'wwtw_sludge_transport_and_disposal',
    u'Result LID Embodied GHG':
    u'result_lid_embodied_ghg',
    u'WWP Annual Maintenance':
    u'wwp_annual_maintenance',
    u'WWCS Unit Weight M1':
    u'wwcs_unit_weight_m1',
    u'RB Design and Capital Costs':
    u'rb_design_and_capital_costs',
    u'Asphalt Construction GHG':
    u'asphalt_construction_ghg',
    u'WDM Daily Maintenance Costs':
    u'wdm_daily_maintenance_costs',
    u'SF Faucet Demand':
    u'sf_faucet_demand',
    u'WWP Daily Energy':
    u'wwp_daily_energy',
    u'Bioretention CN Value':
    u'bioretention_cn_value',
    u'Result Treatment LCC':
    u'result_treatment_lcc',
    u'SF WD per Capita No Measures':
    u'sf_wd_per_capita_no_measures',
    u'Result Pumping GHG Emissions':
    u'result_pumping_ghg_emissions',
    u'WWTW Number of Staff':
    u'wwtw_number_of_staff',
    u'GWS Annual Maintenance Costs':
    u'gws_annual_maintenance_costs',
    u'Landuse4 Daily Nitrogen':
    u'landuse4_daily_nitrogen',
    u'SWTW Running Costs':
    u'swtw_running_costs',
    u'SWP Risk to Human Health':
    u'swp_risk_to_human_health',
    u'PP Construction GHG':
    u'pp_construction_ghg',
    u'MBR Space Requirements':
    u'mbr_space_requirements',
    u'GWS Total LCC':
    u'gws_total_lcc',
    u'SWP Acceptability':
    u'swp_acceptability',
    u'CC Upper VC':
    u'cc_upper_vc',
    u'WTW Operation Energy':
    u'wtw_operation_energy',
    u'RB and Cistern Daily Costs':
    u'rb_and_cistern_daily_costs',
    u'WP Flexibility and Adaptability':
    u'wp_flexibility_and_adaptability',
    u'WWTW Unit Ethanol GHG':
    u'wwtw_unit_ethanol_ghg',
    u'WDM Unit Maintenance Energy M1':
    u'wdm_unit_maintenance_energy_m1',
    u'Green Roof Daily Costs':
    u'green_roof_daily_costs',
    u'Dem OB Restroom':
    u'dem_ob_restroom',
    u'SWT Ferric Chloride':
    u'swt_ferric_chloride',
    u'WTW Unit Carbon Dioxide EmEnergy':
    u'wtw_unit_carbon_dioxide_emenergy',
    u'IA Runoff Coefficient':
    u'ia_runoff_coefficient',
    u'WTW Average Staff Salary':
    u'wtw_average_staff_salary',
    u'WTW Unit Microsand EmEnergy':
    u'wtw_unit_microsand_emenergy',
    u'SWP Affordability':
    u'swp_affordability',
    u'Water Reuse Daily':
    u'water_reuse_daily',
    u'Bioswale Acceptability':
    u'bioswale_acceptability',
    u'LM Installation and Construction':
    u'lm_installation_and_construction',
    u'Bioretention Space Requirements':
    u'bioretention_space_requirements',
    u'PP LCC':
    u'pp_lcc',
    u'SWCS LC Energy Embodied':
    u'swcs_lc_energy_embodied',
    u'Daycares Upper VC':
    u'daycares_upper_vc',
    u'RR Total Urea Generated':
    u'rr_total_urea_generated',
    u'Bioswale Annual Maintenance Costs':
    u'bioswale_annual_maintenance_costs',
    u'RB and Cistern Percentage':
    u'rb_and_cistern_percentage',
    u'LM Daily Energy Consumption':
    u'lm_daily_energy_consumption',
    u'SWT Total Ferric Chloride GHG':
    u'swt_total_ferric_chloride_ghg',
    u'LM Daily GHG Emission':
    u'lm_daily_ghg_emission',
    u'MBR Daily GHG Emission':
    u'mbr_daily_ghg_emission',
    u'WWP Total Energy':
    u'wwp_total_energy',
    u'WWTW Treated Wastewater':
    u'wwtw_treated_wastewater',
    u'Result Pumping LCC':
    u'result_pumping_lcc',
    u'MBR GHG per m3':
    u'mbr_ghg_per_m3',
    u'WTW Administration Costs':
    u'wtw_administration_costs',
    u'Daily Water Demand':
    u'daily_water_demand',
    u'Years':
    u'years',
    u'LM Percentage of Hospitals':
    u'lm_percentage_of_hospitals',
    u'WWCS EmEnergy Maintenance':
    u'wwcs_emenergy_maintenance',
    u'Landuse3 Daily Nitrogen':
    u'landuse3_daily_nitrogen',
    'TIME':
    'time',
    u'MF WD per Capita No Measures':
    u'mf_wd_per_capita_no_measures',
    u'MF Rate of Adoption':
    u'mf_rate_of_adoption',
    u'LU Sum':
    u'lu_sum',
    u'Landuse3 Percentage':
    u'landuse3_percentage',
    u'Unit Irrigation Demand':
    u'unit_irrigation_demand',
    u'GWS Percentage of System Coverage':
    u'gws_percentage_of_system_coverage',
    u'MF New Units':
    u'mf_new_units',
    u'WWTW Total Calcium Hydroxide EmEnergy':
    u'wwtw_total_calcium_hydroxide_emenergy',
    u'Green Roof Affordability':
    u'green_roof_affordability',
    u'WWTW Total Nitric Acid':
    u'wwtw_total_nitric_acid',
    u'Green Roof Runoff Total':
    u'green_roof_runoff_total',
    u'WSC Disposal':
    u'wsc_disposal',
    u'MF Coefficient of Seasonal Variation':
    u'mf_coefficient_of_seasonal_variation',
    u'Result System GHG Emissions':
    u'result_system_ghg_emissions',
    u'WP Reliability':
    u'wp_reliability',
    u'WWTW Unit Methanol EmEnergy':
    u'wwtw_unit_methanol_emenergy',
    u'Distributed Treated Water':
    u'distributed_treated_water',
    u'RWH Space Requirements':
    u'rwh_space_requirements',
    u'WWTW Average Salary':
    u'wwtw_average_salary',
    u'RH Tank Outflow':
    u'rh_tank_outflow',
    u'MBR Daily Maintenance':
    u'mbr_daily_maintenance',
    u'WDM Disposal':
    u'wdm_disposal',
    u'Result RR GHG Emissions':
    u'result_rr_ghg_emissions',
    u'WTW Total Sodium Hypochlorite':
    u'wtw_total_sodium_hypochlorite',
    u'WSC Running Costs':
    u'wsc_running_costs',
    u'WDM Total Length M1':
    u'wdm_total_length_m1',
    u'WDM Total Length M2':
    u'wdm_total_length_m2',
    u'WWP Price per kWh':
    u'wwp_price_per_kwh',
    u'LM Inflow Schools':
    u'lm_inflow_schools',
    u'WWP Risk to Human Health':
    u'wwp_risk_to_human_health',
    u'CC Lower VC':
    u'cc_lower_vc',
    u'WP Daily Maintenance':
    u'wp_daily_maintenance',
    u'WWTW Unit Ethanol EmEnergy':
    u'wwtw_unit_ethanol_emenergy',
    u'SF WD per Capita Water Sensitive':
    u'sf_wd_per_capita_water_sensitive',
    u'WWTW Unit Methanol':
    u'wwtw_unit_methanol',
    u'SWCS Running Costs':
    u'swcs_running_costs',
    u'Result Pumping Energy':
    u'result_pumping_energy',
    u'RR Daily Biogas':
    u'rr_daily_biogas',
    u'PP Design and Capital Costs':
    u'pp_design_and_capital_costs',
    u'GWS Installation Costs':
    u'gws_installation_costs',
    u'MBR Daily Energy Consumption':
    u'mbr_daily_energy_consumption',
    u'RH Control':
    u'rh_control',
    u'SF WEC Toilet':
    u'sf_wec_toilet',
    u'WTW Acceptability':
    u'wtw_acceptability',
    u'WWTW Total Ferric Chloride GHG':
    u'wwtw_total_ferric_chloride_ghg',
    u'Porous Pavement Risk to Human Health':
    u'porous_pavement_risk_to_human_health',
    u'WTW Flexibility and Adaptability':
    u'wtw_flexibility_and_adaptability',
    u'Result System Risk to Human Health':
    u'result_system_risk_to_human_health',
    u'Bioswale Contruction GHG':
    u'bioswale_contruction_ghg',
    u'WWTW Reliability':
    u'wwtw_reliability',
    u'SF Dishwasher Demand':
    u'sf_dishwasher_demand',
    u'Landuse2 Daily Nitrogen':
    u'landuse2_daily_nitrogen',
    u'Bioretention Percentage':
    u'bioretention_percentage',
    u'Retail Lower VC':
    u'retail_lower_vc',
    u'Days With Higher Demand':
    u'days_with_higher_demand',
    u'MBR Risk to Human Health':
    u'mbr_risk_to_human_health',
    u'GWS Risk to Human Health':
    u'gws_risk_to_human_health',
    u'FINAL TIME':
    u'final_time',
    u'WWTW Total Calcium Hydroxide GHG':
    u'wwtw_total_calcium_hydroxide_ghg',
    u'SWCS Construction':
    u'swcs_construction',
    u'WTW Total Alum':
    u'wtw_total_alum',
    u'WWTW Operation Electricity':
    u'wwtw_operation_electricity',
    u'SWCS Unit Maintenance GHG M1':
    u'swcs_unit_maintenance_ghg_m1',
    u'WWCS Total Weight M1':
    u'wwcs_total_weight_m1',
    u'WWCS Total Weight M2':
    u'wwcs_total_weight_m2',
    u'WWTW Unit Nitric Acid':
    u'wwtw_unit_nitric_acid',
    u'RHP Daily Costs':
    u'rhp_daily_costs',
    u'MF WEC Shower':
    u'mf_wec_shower',
    u'WWTW Administration Costs':
    u'wwtw_administration_costs',
    u'WWCS Number of Maintenance Trips':
    u'wwcs_number_of_maintenance_trips',
    u'MF Decommissioned Units Annually':
    u'mf_decommissioned_units_annually',
    u'WP Space Requirements':
    u'wp_space_requirements',
    u'Commercial and Institutional Demand':
    u'commercial_and_institutional_demand',
    u'Utility Years':
    u'utility_years',
    u'RHP Daily Maintenance':
    u'rhp_daily_maintenance',
    u'RWH Flexibility and Adaptability':
    u'rwh_flexibility_and_adaptability',
    u'Qv':
    u'qv',
    u'Restaurants Upper VC':
    u'restaurants_upper_vc',
    u'Dem Community Centers':
    u'dem_community_centers',
    u'GWS Total Volume':
    u'gws_total_volume',
    u'MF WEC Dishwasher':
    u'mf_wec_dishwasher',
    u'Qh':
    u'qh',
    u'GWP Motor Efficiency':
    u'gwp_motor_efficiency',
    u'PP Annual Maintenance Costs':
    u'pp_annual_maintenance_costs',
    u'SWP Construction and Installation':
    u'swp_construction_and_installation',
    u'RHP Annual Maintenance':
    u'rhp_annual_maintenance',
    u'SF Rate of Adoption':
    u'sf_rate_of_adoption',
    u'CC Area':
    u'cc_area',
    u'GWS Plumbing Area':
    u'gws_plumbing_area',
    u'SF Toilet Demand':
    u'sf_toilet_demand',
    u'Green Roof Total Construction GHG':
    u'green_roof_total_construction_ghg',
    u'SW Release Rate':
    u'sw_release_rate',
    u'GWP Total LCC':
    u'gwp_total_lcc',
    u'WWTW Risk to Human Health':
    u'wwtw_risk_to_human_health',
    u'IA Runoff Total':
    u'ia_runoff_total',
    u'WTW Risk to Human Health':
    u'wtw_risk_to_human_health',
    u'Bioswale Reliability':
    u'bioswale_reliability',
    u'WTW Unit Alum GHG':
    u'wtw_unit_alum_ghg',
    u'RWH Reliability':
    u'rwh_reliability',
    u'MF WEC Toilet':
    u'mf_wec_toilet',
    u'GWS Average Size of Tank':
    u'gws_average_size_of_tank',
    u'GWP Daily Maintenance':
    u'gwp_daily_maintenance',
    u'WWTW Total Nitric Acid EmEnergy':
    u'wwtw_total_nitric_acid_emenergy',
    u'WWP Duration of Pump Operation':
    u'wwp_duration_of_pump_operation',
    u'WWP Total LCC':
    u'wwp_total_lcc',
    u'RB and Cistern LCC':
    u'rb_and_cistern_lcc',
    u'Dem Restaurants':
    u'dem_restaurants',
    u'WWTW Affordability':
    u'wwtw_affordability',
    u'MF Toilet Demand':
    u'mf_toilet_demand',
    u'SWP Total Dynamic Head of Pump':
    u'swp_total_dynamic_head_of_pump',
    u'RR Unit GHG Urea':
    u'rr_unit_ghg_urea',
    u'MF Faucet Demand':
    u'mf_faucet_demand',
    u'WDM Total Costs':
    u'wdm_total_costs',
    u'MF Bathtub Demand':
    u'mf_bathtub_demand',
    u'Daycares Lower VC':
    u'daycares_lower_vc',
    u'MBR Installation and Construction Costs':
    u'mbr_installation_and_construction_costs',
    u'WWTW Unit Ethanol':
    u'wwtw_unit_ethanol',
    u'GWS Number of Tanks':
    u'gws_number_of_tanks',
    u'WTM Construction':
    u'wtm_construction',
    u'WWP Flexibility and Adaptability':
    u'wwp_flexibility_and_adaptability',
    u'SWCS Disposal':
    u'swcs_disposal',
    u'RHP Motor Efficiency':
    u'rhp_motor_efficiency',
    u'Restaurant Seats':
    u'restaurant_seats',
    u'SWP Daily Maintenance':
    u'swp_daily_maintenance',
    u'WTW Unit Calcium Hydroxide GHG':
    u'wtw_unit_calcium_hydroxide_ghg',
    u'RR Biogas Generated':
    u'rr_biogas_generated',
    u'WTW Unit Calcium Hydroxide':
    u'wtw_unit_calcium_hydroxide',
    u'WWTW Unit Ferric Sulphate':
    u'wwtw_unit_ferric_sulphate',
    u'RHP Total LCC':
    u'rhp_total_lcc',
    u'WWCS Construction':
    u'wwcs_construction',
    u'WDM Annual Maintenance':
    u'wdm_annual_maintenance',
    u'MBR Annual Maintenance':
    u'mbr_annual_maintenance',
    u'SWCS Construction Energy M1':
    u'swcs_construction_energy_m1',
    u'WTW Reliability':
    u'wtw_reliability',
    u'RWH Acceptability':
    u'rwh_acceptability',
    u'SWTW Unit Ferric Chloride EmEnergy':
    u'swtw_unit_ferric_chloride_emenergy',
    u'MBR Flexibility and Adaptability':
    u'mbr_flexibility_and_adaptability',
    u'WDM Total Weight M1':
    u'wdm_total_weight_m1',
    u'WDM Total Weight M2':
    u'wdm_total_weight_m2',
    u'MF New Units Annually':
    u'mf_new_units_annually',
    u'SWTW Flexibility and Adaptability':
    u'swtw_flexibility_and_adaptability',
    u'RR Total GHG Ammonium Nitrate':
    u'rr_total_ghg_ammonium_nitrate',
    u'MF Units Decomissioned':
    u'mf_units_decomissioned',
    u'WDM Unit Construction Energy M2':
    u'wdm_unit_construction_energy_m2',
    u'WDM Unit Construction Energy M1':
    u'wdm_unit_construction_energy_m1',
    u'SWCS EmEnergy Maintenance':
    u'swcs_emenergy_maintenance',
    u'RR Unit EmEnergy Ammonium Nitrate':
    u'rr_unit_emenergy_ammonium_nitrate',
    u'IA Percentage of Area Collected':
    u'ia_percentage_of_area_collected',
    u'WTW Electricity for treatment of m3':
    u'wtw_electricity_for_treatment_of_m3',
    u'SWCS Unit Maintenance GHG M2':
    u'swcs_unit_maintenance_ghg_m2',
    u'WWCS Construction Energy M2':
    u'wwcs_construction_energy_m2',
    u'WWCS Construction Energy M1':
    u'wwcs_construction_energy_m1',
    u'Utility Months':
    u'utility_months',
    u'Landuse3':
    u'landuse3',
    u'Porous Pavement Space Requirements':
    u'porous_pavement_space_requirements',
    u'WWCS Maintenance GHG':
    u'wwcs_maintenance_ghg',
    u'WTM Replacement':
    u'wtm_replacement',
    u'WDM Unit Maintenance GHG M2':
    u'wdm_unit_maintenance_ghg_m2',
    u'WDM Unit Maintenance GHG M1':
    u'wdm_unit_maintenance_ghg_m1',
    u'WWTW Total Methanol EmEnergy':
    u'wwtw_total_methanol_emenergy',
    u'WWTW Total Nitric Acid GHG':
    u'wwtw_total_nitric_acid_ghg',
    u'GWP Daily Costs':
    u'gwp_daily_costs',
    u'WWCS Running Costs':
    u'wwcs_running_costs',
    u'MBR Reliability':
    u'mbr_reliability',
    u'SWTW Reliability':
    u'swtw_reliability',
    u'Green Roof Risk to Human Health':
    u'green_roof_risk_to_human_health',
    u'SF Average Occupancy per Unit':
    u'sf_average_occupancy_per_unit',
    u'WP Construction and Installation':
    u'wp_construction_and_installation',
    u'WDM Maintenance GHG':
    u'wdm_maintenance_ghg',
    u'WTW Embodied GHG for Chemicals':
    u'wtw_embodied_ghg_for_chemicals',
    u'RR Unit GHG Ammonium Nitrate':
    u'rr_unit_ghg_ammonium_nitrate',
    u'SF Decommissioned Units Annually':
    u'sf_decommissioned_units_annually',
    u'S':
    u's',
    u'LM Inflow Total':
    u'lm_inflow_total',
    u'Unit Demand per Bed':
    u'unit_demand_per_bed',
    u'WWTW Daily Maintenance':
    u'wwtw_daily_maintenance',
    u'WTW Running Costs':
    u'wtw_running_costs',
    u'SWCS Annual Maintenance':
    u'swcs_annual_maintenance',
    u'SF Total Area for Irrigation':
    u'sf_total_area_for_irrigation',
    u'SF WEC Dishwasher':
    u'sf_wec_dishwasher',
    u'SWS Total Length M1':
    u'sws_total_length_m1',
    u'WP Variable Speed Drive Efficiency':
    u'wp_variable_speed_drive_efficiency',
    u'WTM Running Costs':
    u'wtm_running_costs',
    u'Unit Demand Per Student':
    u'unit_demand_per_student',
    u'Unit Industrial Demand Per Floor Area':
    u'unit_industrial_demand_per_floor_area',
    u'Water Conduit Reserved Capacity':
    u'water_conduit_reserved_capacity',
    u'WWCS Unit Maintenance Energy M2':
    u'wwcs_unit_maintenance_energy_m2',
    u'WWCS Unit Maintenance Energy M1':
    u'wwcs_unit_maintenance_energy_m1',
    u'PP CN Value':
    u'pp_cn_value',
    u'Green Roof Flexibility and Adaptability':
    u'green_roof_flexibility_and_adaptability',
    u'GWP Total Energy':
    u'gwp_total_energy',
    u'RB and Cistern Storage Volume':
    u'rb_and_cistern_storage_volume',
    u'Bioswale Risk to Human Health':
    u'bioswale_risk_to_human_health',
    u'Stormwater Tank':
    u'stormwater_tank',
    u'WSC Daily Maintenance':
    u'wsc_daily_maintenance',
    u'WWCS LC Embodied GHG':
    u'wwcs_lc_embodied_ghg',
    u'WTW Total Alum GHG':
    u'wtw_total_alum_ghg',
    u'Unit Demand of Retail Space':
    u'unit_demand_of_retail_space',
    u'Asphalt Unit GHG Emissions':
    u'asphalt_unit_ghg_emissions',
    u'Biretention LCC':
    u'biretention_lcc',
    u'WP Daily Energy':
    u'wp_daily_energy',
    u'MF WEC Leaks':
    u'mf_wec_leaks',
    u'Dem Retail':
    u'dem_retail',
    u'SF Stock of No Measure Units':
    u'sf_stock_of_no_measure_units',
    u'RH Total Water Harvested':
    u'rh_total_water_harvested',
    u'Landuse2 Nitrogen':
    u'landuse2_nitrogen',
    u'LM Total GHG':
    u'lm_total_ghg',
    u'WTW Administration Rate':
    u'wtw_administration_rate',
    u'Wastewater Generation as a percentage of water use':
    u'wastewater_generation_as_a_percentage_of_water_use',
    u'WWTW Staff Costs':
    u'wwtw_staff_costs',
    u'SWCS Maintenance GHG':
    u'swcs_maintenance_ghg',
    u'Months':
    u'months',
    u'Number of Beds':
    u'number_of_beds',
    u'SF WEC Shower':
    u'sf_wec_shower',
    u'RR Total Ammonium Nitrate Generated':
    u'rr_total_ammonium_nitrate_generated',
    u'Water Scarcity Counter':
    u'water_scarcity_counter',
    u'SF Shower Demand':
    u'sf_shower_demand',
    u'MF Stock of Units':
    u'mf_stock_of_units',
    u'Wastewater System Capacity':
    u'wastewater_system_capacity',
    u'WTM Disposal':
    u'wtm_disposal',
    u'SWP Daily Costs':
    u'swp_daily_costs',
    u'PP Percentage':
    u'pp_percentage',
    u'WSC Total Costs':
    u'wsc_total_costs',
    u'SWP Annual Maintenance':
    u'swp_annual_maintenance',
    u'WWTW Running Costs':
    u'wwtw_running_costs',
    u'WP Total Energy':
    u'wp_total_energy',
    u'WDM Unit Construction GHG M2':
    u'wdm_unit_construction_ghg_m2',
    u'SF Average Lot Size':
    u'sf_average_lot_size',
    u'WDM Unit Construction GHG M1':
    u'wdm_unit_construction_ghg_m1',
    u'SF Clothes Washer Demand':
    u'sf_clothes_washer_demand',
    u'WTW Total Microsand GHG':
    u'wtw_total_microsand_ghg',
    u'GWS Plumbing Costs per m2':
    u'gws_plumbing_costs_per_m2',
    u'WTW Unit Alum':
    u'wtw_unit_alum',
    u'WWCS Daily Maintenance':
    u'wwcs_daily_maintenance',
    u'LM Total LCC':
    u'lm_total_lcc',
    u'SWTW Risk to Human Health':
    u'swtw_risk_to_human_health',
    u'WTW Staff Costs':
    u'wtw_staff_costs',
    u'Bioretention Reliability':
    u'bioretention_reliability',
    u'Bioretention Total Construction GHG':
    u'bioretention_total_construction_ghg',
    u'PP Total Construction GHG':
    u'pp_total_construction_ghg',
    u'GWP Average Dynamic Head':
    u'gwp_average_dynamic_head',
    u'WTW Total Polyaluminium Chloride':
    u'wtw_total_polyaluminium_chloride',
    u'WWTW Total Ferric Sulphate':
    u'wwtw_total_ferric_sulphate',
    u'SAVEPER':
    u'saveper',
    u'WWCS Unit Weight M2':
    u'wwcs_unit_weight_m2',
    u'WTW Unit Sodium Hypochlorite':
    u'wtw_unit_sodium_hypochlorite',
    u'SWP Total GHG Emission':
    u'swp_total_ghg_emission',
    u'WWTW Unit Nitric Acid EmEnergy':
    u'wwtw_unit_nitric_acid_emenergy',
    u'Wastewater Treated':
    u'wastewater_treated',
    u'Number of Children':
    u'number_of_children',
    u'Asphalt Capital Costs':
    u'asphalt_capital_costs',
    u'GWS Flexibility and Adaptability':
    u'gws_flexibility_and_adaptability',
    u'SF New Units':
    u'sf_new_units',
    u'WWCS Unit Maintenance GHG M2':
    u'wwcs_unit_maintenance_ghg_m2',
    u'Bioretention Flexibility and Adaptability':
    u'bioretention_flexibility_and_adaptability',
    u'WWCS Unit Maintenance GHG M1':
    u'wwcs_unit_maintenance_ghg_m1',
    u'CC Unit Demand':
    u'cc_unit_demand',
    u'Bioswale Affordability':
    u'bioswale_affordability',
    u'SWCS Total Length M2':
    u'swcs_total_length_m2',
    u'Result System Space Requirements':
    u'result_system_space_requirements',
    u'Industrial Demand Variation Coefficient':
    u'industrial_demand_variation_coefficient',
    u'WWCS Annual Maintenance':
    u'wwcs_annual_maintenance',
    u'INITIAL TIME':
    u'initial_time',
    u'WTW Unit Polyaluminium Chloride EmEnergy':
    u'wtw_unit_polyaluminium_chloride_emenergy',
    u'Industrial Demand':
    u'industrial_demand',
    u'WWTW Total Methanol GHG':
    u'wwtw_total_methanol_ghg',
    u'WTW Annual Maintenance':
    u'wtw_annual_maintenance',
    u'HVAC Hours of Operation':
    u'hvac_hours_of_operation',
    u'GWP Number of Pumps':
    u'gwp_number_of_pumps',
    u'LM GHG per m3':
    u'lm_ghg_per_m3',
    u'RR Daily Ammonium Nitrate':
    u'rr_daily_ammonium_nitrate',
    u'GWP Annual Maintenance':
    u'gwp_annual_maintenance',
    u'RR Total EmEnergy Urea':
    u'rr_total_emenergy_urea',
    u'WWP Daily Maintenance':
    u'wwp_daily_maintenance',
    u'WTW Unit Polyaluminium Chloride':
    u'wtw_unit_polyaluminium_chloride',
    u'WWCS Total Length M1':
    u'wwcs_total_length_m1',
    u'WWCS Total Length M2':
    u'wwcs_total_length_m2',
    u'Landuse1 Nitrogen':
    u'landuse1_nitrogen',
    u'RHP Number of Pumps':
    u'rhp_number_of_pumps',
    u'SWCS Unit Construction GHG M1':
    u'swcs_unit_construction_ghg_m1',
    u'SWCS Unit Construction GHG M2':
    u'swcs_unit_construction_ghg_m2',
    u'WWCS Replacement':
    u'wwcs_replacement',
    u'MF Leaks':
    u'mf_leaks',
    u'Weeks':
    u'weeks',
    u'Landuse4 Nitrogen':
    u'landuse4_nitrogen',
    u'MF Initial Stock of Units':
    u'mf_initial_stock_of_units',
    u'Result System Energy':
    u'result_system_energy',
    u'Green Roof Space Requirements':
    u'green_roof_space_requirements',
    u'LM Inflow Office Buildings':
    u'lm_inflow_office_buildings',
    u'SWP Duration of Pump Operation':
    u'swp_duration_of_pump_operation',
    u'Landuse3 EMC Nitrogen':
    u'landuse3_emc_nitrogen',
    u'WWTW Unit Ferric Sulphate EmEnergy':
    u'wwtw_unit_ferric_sulphate_emenergy',
    u'Landuse3 Nitrogen':
    u'landuse3_nitrogen',
    u'RHP Total GHG Emission':
    u'rhp_total_ghg_emission',
    u'Green Roof Annual Maintenance Costs':
    u'green_roof_annual_maintenance_costs',
    u'WWTW Total Ferric Sulphate EmEnergy':
    u'wwtw_total_ferric_sulphate_emenergy',
    u'SWP Pump Efficiency':
    u'swp_pump_efficiency',
    u'CN Composite':
    u'cn_composite',
    u'WWCS LC Embodied Energy':
    u'wwcs_lc_embodied_energy',
    u'RHP Total Energy':
    u'rhp_total_energy',
    u'WWTW Unit Ferric Sulphate GHG':
    u'wwtw_unit_ferric_sulphate_ghg',
    u'Result RR Energy':
    u'result_rr_energy',
    u'WWP Motor Efficiency':
    u'wwp_motor_efficiency',
    u'LM Annual Maintenance':
    u'lm_annual_maintenance',
    u'WWTW Unit Calcium Hydroxide EmEnergy':
    u'wwtw_unit_calcium_hydroxide_emenergy',
    u'WWTW Total Ethanol GHG':
    u'wwtw_total_ethanol_ghg',
    u'WTW Unit Carbon Dioxide':
    u'wtw_unit_carbon_dioxide',
    u'Landuse Total Nitrogen':
    u'landuse_total_nitrogen',
    u'SWP Motor Efficiency':
    u'swp_motor_efficiency',
    u'Domestic Demand':
    u'domestic_demand',
    u'SWCS Construction GHG M2':
    u'swcs_construction_ghg_m2',
    u'SWCS Construction GHG M1':
    u'swcs_construction_ghg_m1',
    u'WDM Replacement':
    u'wdm_replacement',
    u'RHP Daily GHG Emissions':
    u'rhp_daily_ghg_emissions',
    u'Porous Pavement Reliability':
    u'porous_pavement_reliability',
    u'WP Unit Conversion Factor':
    u'wp_unit_conversion_factor',
    u'IA Standard Roof Footprint':
    u'ia_standard_roof_footprint',
    u'Result Treatment Embodied Energy':
    u'result_treatment_embodied_energy',
    u'Coefficient of Seasonal Variation in Irrigation Demand':
    u'coefficient_of_seasonal_variation_in_irrigation_demand',
    u'SWCS Unit Weight M1':
    u'swcs_unit_weight_m1',
    u'WP Acceptability':
    u'wp_acceptability',
    u'WTW Total Polyaluminium Chloride GHG':
    u'wtw_total_polyaluminium_chloride_ghg',
    u'WTW Total Carbon Dioxide':
    u'wtw_total_carbon_dioxide',
    u'Bioswale Total Construction GHG':
    u'bioswale_total_construction_ghg',
    u'SWP Total LCC':
    u'swp_total_lcc',
    u'Footprint Hotels':
    u'footprint_hotels',
    u'MF WEC Clothes Washer':
    u'mf_wec_clothes_washer',
    u'HVAC Demand Variation Coefficient':
    u'hvac_demand_variation_coefficient',
    u'RR Unit Ammonium Nitrate':
    u'rr_unit_ammonium_nitrate',
    u'SF Bathtub Demand':
    u'sf_bathtub_demand',
    u'WWTW Unit Calcium Hydroxide':
    u'wwtw_unit_calcium_hydroxide',
    u'Bioswale Footprint':
    u'bioswale_footprint',
    u'WWTW Total Ferric Chloride':
    u'wwtw_total_ferric_chloride',
    u'WWP Daily GHG Emissions':
    u'wwp_daily_ghg_emissions',
    u'WWTW Annual Maintenance':
    u'wwtw_annual_maintenance',
    u'RR Unit Biogas':
    u'rr_unit_biogas',
    u'SWCS Unit Maintenance Energy M1':
    u'swcs_unit_maintenance_energy_m1',
    u'Landuse1 Daily Nitrogen':
    u'landuse1_daily_nitrogen',
    u'SWCS Number of Maintenance Trips':
    u'swcs_number_of_maintenance_trips',
    u'WWTW Unit Calcium Hydroxide GHG':
    u'wwtw_unit_calcium_hydroxide_ghg',
    u'WDM Number of Maintenance Trips':
    u'wdm_number_of_maintenance_trips',
    u'MF Stock of No Measure Units':
    u'mf_stock_of_no_measure_units',
    u'GWP Daily Energy':
    u'gwp_daily_energy',
    u'WSC Replacement':
    u'wsc_replacement',
    u'SWTW Staff Costs':
    u'swtw_staff_costs',
    u'LM Reliability':
    u'lm_reliability',
    u'LM Percentage of Schools':
    u'lm_percentage_of_schools',
    u'WWCS Construction GHG M2':
    u'wwcs_construction_ghg_m2',
    u'WWCS Construction GHG M1':
    u'wwcs_construction_ghg_m1',
    u'Bioretention Acceptability':
    u'bioretention_acceptability',
    u'WTW Capital Investment':
    u'wtw_capital_investment',
    u'SWTW Space Requirements':
    u'swtw_space_requirements',
    u'Result LID LCC':
    u'result_lid_lcc',
    u'WDM Construction Energy M1':
    u'wdm_construction_energy_m1',
    u'WDM Construction Energy M2':
    u'wdm_construction_energy_m2',
    u'Electricity Fee':
    u'electricity_fee',
    u'MBR Acceptability':
    u'mbr_acceptability',
    u'WP CO2 per kWh':
    u'wp_co2_per_kwh',
    u'RHP Pump Efficiency':
    u'rhp_pump_efficiency',
    u'RHP Construction and Installation':
    u'rhp_construction_and_installation',
    u'WWTW Total Costs':
    u'wwtw_total_costs',
    u'RHP Variable Speed Drive Efficiency':
    u'rhp_variable_speed_drive_efficiency',
    u'WWTW Total Ethanol EmEnergy':
    u'wwtw_total_ethanol_emenergy',
    u'Dem Hospitals Restroom':
    u'dem_hospitals_restroom',
    u'Bioswale CN Value':
    u'bioswale_cn_value',
    u'Green Roof Percentage':
    u'green_roof_percentage',
    u'WWP Variable Speed Drive Efficiency':
    u'wwp_variable_speed_drive_efficiency',
    u'WTW Unit Sodium Hypochlorite GHG':
    u'wtw_unit_sodium_hypochlorite_ghg',
    u'Water Conduit Daily Capacity':
    u'water_conduit_daily_capacity',
    u'RB and Cistern CN Value':
    u'rb_and_cistern_cn_value',
    u'Bioretention Annual Maintenance Costs':
    u'bioretention_annual_maintenance_costs',
    u'LM Risk to Human Health':
    u'lm_risk_to_human_health',
    u'Dem Schools':
    u'dem_schools',
    u'WTW Unit Calcium Hydroxide EmEnergy':
    u'wtw_unit_calcium_hydroxide_emenergy',
    u'IA Runoff Daily':
    u'ia_runoff_daily',
    u'WDM EmEnergy Maintenance':
    u'wdm_emenergy_maintenance',
    u'GWP Current Storage Volume':
    u'gwp_current_storage_volume',
    u'WP Total GHG Emission':
    u'wp_total_ghg_emission',
    u'WTW Total Sodium Hypochlorite EmEnergy':
    u'wtw_total_sodium_hypochlorite_emenergy',
    u'Unit Demand per Child':
    u'unit_demand_per_child',
    u'MF WEC Faucet':
    u'mf_wec_faucet',
    u'SWP Reliability':
    u'swp_reliability',
    u'WP Price per kWh':
    u'wp_price_per_kwh',
    u'MF Shower Demand':
    u'mf_shower_demand',
    u'Result Treatment GHG Emissions':
    u'result_treatment_ghg_emissions',
    u'LN Number of LM':
    u'ln_number_of_lm',
    u'Asphalt Unit Energy':
    u'asphalt_unit_energy',
    u'WDM LC Embodied Energy':
    u'wdm_lc_embodied_energy',
    u'WTW Unit Alum EmEnergy':
    u'wtw_unit_alum_emenergy',
    u'WTW Unit Microsand GHG':
    u'wtw_unit_microsand_ghg',
    u'WTW Total Microsand EmEnergy':
    u'wtw_total_microsand_emenergy',
    u'GHG Emission Generation Electricity Factor':
    u'ghg_emission_generation_electricity_factor',
    u'SF Units Total Area Occupied':
    u'sf_units_total_area_occupied',
    u'WTW Space Requirements':
    u'wtw_space_requirements',
    u'RWH Risk to Human Health':
    u'rwh_risk_to_human_health',
    u'WTW Number of Staff':
    u'wtw_number_of_staff',
    u'WWP Reliability':
    u'wwp_reliability',
    u'Green Roof C Coefficient':
    u'green_roof_c_coefficient',
    u'MBR Total GHG Emission':
    u'mbr_total_ghg_emission',
    u'Unit Demand per Seat':
    u'unit_demand_per_seat',
    u'GWP Duration of Pump Operation':
    u'gwp_duration_of_pump_operation',
    u'RR Total EmEnergy Ammonium Nitrate':
    u'rr_total_emenergy_ammonium_nitrate',
    u'Green Roof CN Value':
    u'green_roof_cn_value',
    u'Porous Pavement Acceptability':
    u'porous_pavement_acceptability',
    u'Dem Hospitals':
    u'dem_hospitals',
    u'IA Parking Footprint':
    u'ia_parking_footprint',
    u'SWTW Annual Maintenance':
    u'swtw_annual_maintenance',
    u'WDM Unit Maintenance Energy M2':
    u'wdm_unit_maintenance_energy_m2',
    u'MF Stock of Water Sensitive Units':
    u'mf_stock_of_water_sensitive_units',
    u'Result System Affordability':
    u'result_system_affordability',
    u'Bioretention Footprint':
    u'bioretention_footprint',
    u'WWP Construction and Installation':
    u'wwp_construction_and_installation',
    u'GWS Acceptability':
    u'gws_acceptability',
    u'SWCS LC Embodied GHG':
    u'swcs_lc_embodied_ghg',
    u'Landuse2 Percentage':
    u'landuse2_percentage',
    u'Result RR LCC':
    u'result_rr_lcc',
    u'Green Roof Acceptability':
    u'green_roof_acceptability',
    u'SWP Flexibility and Adaptability':
    u'swp_flexibility_and_adaptability',
    u'WTW Reserved Treatment Capacity':
    u'wtw_reserved_treatment_capacity',
    u'SWTW Acceptability':
    u'swtw_acceptability',
    u'MBR Capacity':
    u'mbr_capacity',
    u'Dem Daycares':
    u'dem_daycares',
    u'MF WEC Bathtub':
    u'mf_wec_bathtub',
    u'WTW Unit Polyaluimium Chloride GHG':
    u'wtw_unit_polyaluimium_chloride_ghg',
    u'SWCS Unit Maintenance Energy M2':
    u'swcs_unit_maintenance_energy_m2',
    u'SWTW Electricity for treatment':
    u'swtw_electricity_for_treatment',
    u'WWTW Electricity for treatment of m3':
    u'wwtw_electricity_for_treatment_of_m3',
    u'Industrial Floor Area':
    u'industrial_floor_area',
    u'CN4':
    u'cn4',
    u'CN2':
    u'cn2',
    u'CN3':
    u'cn3',
    u'CN1':
    u'cn1',
    u'WWTW Unit Ferric Chloride EmEnergy':
    u'wwtw_unit_ferric_chloride_emenergy',
    u'WP Motor Efficiency':
    u'wp_motor_efficiency',
    u'GWP Total GHG Emission':
    u'gwp_total_ghg_emission',
    u'WWTW Total Calcium Hydroxide':
    u'wwtw_total_calcium_hydroxide',
    u'LM Daily Maintenance':
    u'lm_daily_maintenance',
    u'OB Lower VC':
    u'ob_lower_vc',
    u'WWP Acceptability':
    u'wwp_acceptability',
    u'SF Units Decomissioned':
    u'sf_units_decomissioned',
    u'WTW Operation Daily Energy':
    u'wtw_operation_daily_energy',
    u'Treated Water':
    u'treated_water',
    u'WTW Construction and Installation':
    u'wtw_construction_and_installation',
    u'Bioretention Affordability':
    u'bioretention_affordability',
    u'WWP Pump Efficiency':
    u'wwp_pump_efficiency',
    u'WTW Unit Carbon Dioxide GHG':
    u'wtw_unit_carbon_dioxide_ghg',
    u'RHP Duration of Pump Operation':
    u'rhp_duration_of_pump_operation',
    u'Bioretention Daily Costs':
    u'bioretention_daily_costs',
    u'WWTW Unit Ferric Chloride GHG':
    u'wwtw_unit_ferric_chloride_ghg',
    u'WP Daily Costs':
    u'wp_daily_costs',
    u'Treated Wastewater':
    u'treated_wastewater',
    u'System Water Capacity':
    u'system_water_capacity',
    u'WWTW Total Ferric Sulphate GHG':
    u'wwtw_total_ferric_sulphate_ghg',
    u'WP Annual Maintenance':
    u'wp_annual_maintenance',
    u'Result System Flexibility and Adaptability':
    u'result_system_flexibility_and_adaptability',
    u'WTW Total Microsand':
    u'wtw_total_microsand',
    u'IA Roads and Sidewalks Footprint':
    u'ia_roads_and_sidewalks_footprint',
    u'SWTW Number of Staff':
    u'swtw_number_of_staff',
    u'RH Tank Current Storage Volume':
    u'rh_tank_current_storage_volume',
    u'WSC Annual Maintenance':
    u'wsc_annual_maintenance',
    u'SWCS Unit Weight M2':
    u'swcs_unit_weight_m2',
    u'WWP Total GHG Emission':
    u'wwp_total_ghg_emission',
    u'WP Daily GHG Emissions':
    u'wp_daily_ghg_emissions',
    u'SWP Daily Energy':
    u'swp_daily_energy'
}

__pysd_version__ = "0.9.0"


@cache('run')
def footprint_office_buildings():
    """
    Real Name: Footprint Office Buildings
    Original Eqn: 500000
    Units: m2
    Limits: (None, None)
    Type: constant

    m2 of Office Buildings in new development according to Source: Water \n    \t\tResources Engineering, Larry W Mays, 2001 (Table 11.1.4. Page 346)
    """
    return 500000


@cache('step')
def rh_system_total_construction_ghg():
    """
    Real Name: RH System Total Construction GHG
    Original Eqn: RB and Cistern Storage Volume*RH System Construction GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return rb_and_cistern_storage_volume() * rh_system_construction_ghg()


@cache('step')
def wwp_total_lcc():
    """
    Real Name: WWP Total LCC
    Original Eqn: INTEG ( WWP Daily Costs, WWP Construction and Installation)
    Units: $
    Limits: (None, None)
    Type: component

    Costs of Pumping Station Installation
    """
    return integ_wwp_total_lcc()


@cache('step')
def commercial_and_institutional_demand():
    """
    Real Name: Commercial and Institutional Demand
    Original Eqn: (Dem Hotels + Dem Office Buildings + Dem Restaurants + Dem Schools + Dem Hospitals +\\ Dem Retail + Dem Daycares + Dem Community Centers + Dem HVAC ) * 0.001
    Units: m3/Day
    Limits: (None, None)
    Type: component

    Total Commercial and Insitutional Water Demand Per Day in m3
    """
    return (dem_hotels() + dem_office_buildings() + dem_restaurants() + dem_schools() +
            dem_hospitals() + dem_retail() + dem_daycares() + dem_community_centers() +
            dem_hvac()) * 0.001


integ_rhp_total_ghg_emission = functions.Integ(lambda: rhp_daily_ghg_emissions(), lambda: 0)


@cache('step')
def landuse2_nitrogen():
    """
    Real Name: Landuse2 Nitrogen
    Original Eqn: INTEG ( Landuse2 Daily Nitrogen, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_landuse2_nitrogen()


@cache('run')
def lm_maximum_daily_capacity():
    """
    Real Name: LM Maximum Daily Capacity
    Original Eqn: 1500
    Units: m3/Day
    Limits: (None, None)
    Type: constant

    Prices for 151 m3/day, 302 m3/day, 3785 m3/day
    """
    return 1500


integ_wwp_total_lcc = functions.Integ(lambda: wwp_daily_costs(),
                                      lambda: wwp_construction_and_installation())


@cache('run')
def swtw_capital_investment():
    """
    Real Name: SWTW Capital Investment
    Original Eqn: 1.2
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 1.2


@cache('run')
def gws_percentage_of_system_coverage():
    """
    Real Name: GWS Percentage of System Coverage
    Original Eqn: 0.7
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.7


@cache('run')
def wwtw_construction_and_installation():
    """
    Real Name: WWTW Construction and Installation
    Original Eqn: 0
    Units: $
    Limits: (None, None)
    Type: constant

    Wastewater Treatment Plant Costs (in Millions of $)
    """
    return 0


@cache('run')
def bioretention_space_requirements():
    """
    Real Name: Bioretention Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def dem_schools():
    """
    Real Name: Dem Schools
    Original Eqn: Number of Students*Unit Demand Per Student*Schools Demand Variation Coefficient
    Units: L/Day
    Limits: (None, None)
    Type: component


    """
    return number_of_students() * unit_demand_per_student() * schools_demand_variation_coefficient(
    )


@cache('run')
def lm_reliability():
    """
    Real Name: LM Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def rhp_annual_maintenance():
    """
    Real Name: RHP Annual Maintenance
    Original Eqn: 0
    Units: $
    Limits: (None, None)
    Type: constant

    Percentage of Initial Costs
    """
    return 0


@cache('step')
def wastewater_treated():
    """
    Real Name: Wastewater Treated
    Original Eqn: IF THEN ELSE( Wastewater Generated>=Wastewater System Capacity , Wastewater System Capacity\\ , Wastewater Generated )
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(wastewater_generated() >= wastewater_system_capacity(),
                                  wastewater_system_capacity(), wastewater_generated())


@cache('run')
def landuse4_emc_nitrogen():
    """
    Real Name: Landuse4 EMC Nitrogen
    Original Eqn: 1.3
    Units: mg/L
    Limits: (0.4, 5.5)
    Type: constant

    LTHIA-LID EMC Concetration Value Matrix for Commercila, Industrial, \n    \t\tResidential, Grass pasture, Agriculture, Forest
    """
    return 1.3


@cache('run')
def water_conduit_daily_capacity():
    """
    Real Name: Water Conduit Daily Capacity
    Original Eqn: 15000
    Units: m3/Day
    Limits: (None, None)
    Type: constant

    Maximum Daily Capacity of Water Intake in cubic meters / day
    """
    return 15000


integ_swtw_total_costs = functions.Integ(
    lambda: swtw_running_costs(),
    lambda: (swtw_construction_and_installation() + swtw_capital_investment()) * 10**6)


@cache('step')
def wsc_daily_maintenance():
    """
    Real Name: WSC Daily Maintenance
    Original Eqn: WSC Annual Maintenance / 365.25
    Units: $/Day
    Limits: (None, None)
    Type: component

    Daily costs
    """
    return wsc_annual_maintenance() / 365.25


@cache('run')
def wwtw_risk_to_human_health():
    """
    Real Name: WWTW Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 4


@cache('run')
def retail_upper_vc():
    """
    Real Name: Retail Upper VC
    Original Eqn: 1.33
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1.33


@cache('run')
def wwtw_administration_rate():
    """
    Real Name: WWTW Administration Rate
    Original Eqn: 0.5
    Units: $/Day
    Limits: (None, None)
    Type: constant

    50% of Staff Costs, Daily
    """
    return 0.5


@cache('run')
def sf_wec_dishwasher():
    """
    Real Name: SF WEC Dishwasher
    Original Eqn: 0.53
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.53


@cache('run')
def swp_reliability():
    """
    Real Name: SWP Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('step')
def result_reached_system_capacity():
    """
    Real Name: Result Reached System Capacity
    Original Eqn: INTEG ( Days With Higher Demand, 0)
    Units: Day
    Limits: (None, None)
    Type: component

    Incapacity of Raw Water Intake to Transfer Water
    """
    return integ_result_reached_system_capacity()


@cache('run')
def green_roof_c_coefficient():
    """
    Real Name: Green Roof C Coefficient
    Original Eqn: 0.45
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.45


@cache('step')
def green_roof_lcc():
    """
    Real Name: Green Roof LCC
    Original Eqn: INTEG ( Green Roof Daily Costs, Green Roof Design and Capital Costs * Green Roof Footprint)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_green_roof_lcc()


@cache('run')
def sf_wec_leaks():
    """
    Real Name: SF WEC Leaks
    Original Eqn: 0.7
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.7


@cache('step')
def wwtw_total_methanol_ghg():
    """
    Real Name: WWTW Total Methanol GHG
    Original Eqn: WWTW Total Methanol*WWTW Unit Methanol GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_methanol() * wwtw_unit_methanol_ghg()


@cache('step')
def asphalt_capital_costs():
    """
    Real Name: Asphalt Capital Costs
    Original Eqn: (IA Parking Footprint + IA Roads and Sidewalks Footprint)*Asphalt CC Unit Cost
    Units: $
    Limits: (None, None)
    Type: component


    """
    return (ia_parking_footprint() + ia_roads_and_sidewalks_footprint()) * asphalt_cc_unit_cost()


integ_mf_stock_of_units = functions.Integ(lambda: mf_new_units() - mf_units_decomissioned(),
                                          lambda: mf_initial_stock_of_units())


@cache('step')
def rr_total_emenergy_urea():
    """
    Real Name: RR Total EmEnergy Urea
    Original Eqn: RR Total Urea Generated*RR Unit EmEnergy Urea
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return rr_total_urea_generated() * rr_unit_emenergy_urea()


@cache('run')
def wwtw_unit_ferric_sulphate_ghg():
    """
    Real Name: WWTW Unit Ferric Sulphate GHG
    Original Eqn: 0.37
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.37


@cache('run')
def mf_dishwasher_demand():
    """
    Real Name: MF Dishwasher Demand
    Original Eqn: 4
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 4


@cache('step')
def result_system_acceptability():
    """
    Real Name: Result System Acceptability
    Original Eqn: Bioretention Acceptability + Bioswale Acceptability +Green Roof Acceptability+GWS Acceptability\\ +LM Acceptability+MBR Acceptability+Porous Pavement Acceptability+RWH Acceptability\\ +SWP Acceptability+SWTW Acceptability+WP Acceptability+WTW Acceptability+WWP Acceptability\\ +WWTW Acceptability
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return bioretention_acceptability() + bioswale_acceptability(
    ) + green_roof_acceptability() + gws_acceptability() + lm_acceptability() + mbr_acceptability(
    ) + porous_pavement_acceptability() + rwh_acceptability() + swp_acceptability(
    ) + swtw_acceptability() + wp_acceptability() + wtw_acceptability() + wwp_acceptability(
    ) + wwtw_acceptability()


@cache('step')
def wp_total_lcc():
    """
    Real Name: WP Total LCC
    Original Eqn: INTEG ( WP Daily Costs, WP Construction and Installation)
    Units: $
    Limits: (None, None)
    Type: component

    Costs of Pumping Station Installation
    """
    return integ_wp_total_lcc()


@cache('step')
def wwtw_total_calcium_hydroxide():
    """
    Real Name: WWTW Total Calcium Hydroxide
    Original Eqn: INTEG ( Treated Wastewater*WWTW Unit Calcium Hydroxide, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wwtw_total_calcium_hydroxide()


@cache('run')
def wwp_variable_speed_drive_efficiency():
    """
    Real Name: WWP Variable Speed Drive Efficiency
    Original Eqn: 88
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Variable Speed Drive Efficiency [%]
    """
    return 88


integ_wtw_operation_energy = functions.Integ(lambda: wtw_operation_daily_energy(), lambda: 0)


integ_wtw_embodied_ghg_for_chemicals = functions.Integ(lambda: wtw_total_polyaluminium_chloride_ghg()+wtw_total_alum_ghg()+wtw_total_calcium_hydroxide_ghg()+wtw_total_carbon_dioxide_ghg()+wtw_total_microsand_ghg()+wtw_total_sodium_hypochlorite_ghg(), lambda: 0)


@cache('run')
def wwcs_total_length_m2():
    """
    Real Name: WWCS Total Length M2
    Original Eqn: 2500
    Units: m
    Limits: (None, None)
    Type: constant


    """
    return 2500


@cache('run')
def wwcs_total_length_m1():
    """
    Real Name: WWCS Total Length M1
    Original Eqn: 4500
    Units: m
    Limits: (None, None)
    Type: constant

    Length of Stormwater System
    """
    return 4500


@cache('step')
def swcs_emenergy_maintenance():
    """
    Real Name: SWCS EmEnergy Maintenance
    Original Eqn: ((SWS Total Length M1*SWCS Unit Maintenance Energy M1)+(SWCS Unit Maintenance Energy M2\\ *SWCS Total Length M2))*SWCS Number of Maintenance Trips
    Units: KWh/Day
    Limits: (None, None)
    Type: component


    """
    return ((sws_total_length_m1() * swcs_unit_maintenance_energy_m1()) +
            (swcs_unit_maintenance_energy_m2() * swcs_total_length_m2())
            ) * swcs_number_of_maintenance_trips()


@cache('run')
def rwh_reliability():
    """
    Real Name: RWH Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def swtw_risk_to_human_health():
    """
    Real Name: SWTW Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def mf_wec_clothes_washer():
    """
    Real Name: MF WEC Clothes Washer
    Original Eqn: 1
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Water Efficiency Coefficient - Random
    """
    return 1


@cache('step')
def gwp_current_storage_volume():
    """
    Real Name: GWP Current Storage Volume
    Original Eqn: INTEG ( GWS Tank Inflow-GWS Tank Outflow, 0)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return integ_gwp_current_storage_volume()


integ_wwcs_lc_embodied_ghg = functions.Integ(
    lambda: wwcs_maintenance_ghg(),
    lambda: wwcs_construction_ghg_m1() + wwcs_construction_ghg_m2())


@cache('step')
def result_system_space_requirements():
    """
    Real Name: Result System Space Requirements
    Original Eqn: Bioretention Space Requirements+Bioswale Space Requirements+Green Roof Space Requirements\\ +GWS Space Requirements+LM Space Requirements+MBR Space Requirements+RWH Space Requirements\\ +Porous Pavement Space Requirements+SWP Space Requirements+SWTW Space Requirements+\\ WP Space Requirements+WTW Space Requirements+WWP Space Requirements+WWTW Space Requirements
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return bioretention_space_requirements() + bioswale_space_requirements(
    ) + green_roof_space_requirements() + gws_space_requirements() + lm_space_requirements(
    ) + mbr_space_requirements() + rwh_space_requirements() + porous_pavement_space_requirements(
    ) + swp_space_requirements() + swtw_space_requirements() + wp_space_requirements(
    ) + wtw_space_requirements() + wwp_space_requirements() + wwtw_space_requirements()


@cache('run')
def mf_decommissioned_units_annually():
    """
    Real Name: MF Decommissioned Units Annually
    Original Eqn: 150
    Units: MF Units
    Limits: (None, None)
    Type: constant

    Defined by USER
    """
    return 150


@cache('step')
def green_roof_runoff_daily():
    """
    Real Name: Green Roof Runoff Daily
    Original Eqn: (Green Roof C Coefficient * Green Roof Footprint * Rainfall)/1000
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return (green_roof_c_coefficient() * green_roof_footprint() * rainfall()) / 1000


@cache('run')
def wtw_unit_sodium_hypochlorite_ghg():
    """
    Real Name: WTW Unit Sodium Hypochlorite GHG
    Original Eqn: 0.89
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.89


@cache('run')
def bioswale_risk_to_human_health():
    """
    Real Name: Bioswale Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('step')
def bioswale_total_construction_ghg():
    """
    Real Name: Bioswale Total Construction GHG
    Original Eqn: Bioswale Contruction GHG*Bioswale Footprint
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return bioswale_contruction_ghg() * bioswale_footprint()


@cache('step')
def mf_new_units():
    """
    Real Name: MF New Units
    Original Eqn: INTEGER( MF New Units Annually / Days in a Year )
    Units: MF Units / Day
    Limits: (None, None)
    Type: component


    """
    return int(mf_new_units_annually() / days_in_a_year())


@cache('step')
def lm_inflow_schools():
    """
    Real Name: LM Inflow Schools
    Original Eqn: Dem Schools*Dem Schools Restrooms*LM Percentage of Schools
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return dem_schools() * dem_schools_restrooms() * lm_percentage_of_schools()


@cache('step')
def wtm_running_costs():
    """
    Real Name: WTM Running Costs
    Original Eqn: WTM Daily Maintenance
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return wtm_daily_maintenance()


@cache('step')
def wwp_total_energy():
    """
    Real Name: WWP Total Energy
    Original Eqn: INTEG ( WWP Daily Energy, 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_wwp_total_energy()


@cache('run')
def wwtw_unit_methanol_ghg():
    """
    Real Name: WWTW Unit Methanol GHG
    Original Eqn: 0.736
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.736


@cache('run')
def mf_bathtub_demand():
    """
    Real Name: MF Bathtub Demand
    Original Eqn: 6
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 6


@cache('run')
def wdm_disposal():
    """
    Real Name: WDM Disposal
    Original Eqn: 0
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def swp_total_ghg_emission():
    """
    Real Name: SWP Total GHG Emission
    Original Eqn: INTEG ( SWP Daily GHG Emissions, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_swp_total_ghg_emission()


@cache('step')
def wdm_total_costs():
    """
    Real Name: WDM Total Costs
    Original Eqn: INTEG ( WDM Running Costs, WDM Construction + WDM Replacement + WDM Disposal)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_wdm_total_costs()


@cache('step')
def wwp_daily_energy():
    """
    Real Name: WWP Daily Energy
    Original Eqn: (Wastewater Treated * 0.0115741 * WWP Duration of Pump Operation * WWP Total Dynamic Head\\ * WWP Unit Conversion Factor )/(WWP Motor Efficiency * WWP Pump Efficiency * WWP Variable Speed Drive Efficiency)
    Units: KWh/Day
    Limits: (None, None)
    Type: component

    Daily Energy Consumption required for Drinking Water Pumping\t\t* 0.0115741 Conversion factor m3/day in liters/second
    """
    return (
        wastewater_treated() * 0.0115741 * wwp_duration_of_pump_operation() *
        wwp_total_dynamic_head() * wwp_unit_conversion_factor()) / (
            wwp_motor_efficiency() * wwp_pump_efficiency() * wwp_variable_speed_drive_efficiency())


@cache('step')
def result_system_risk_to_human_health():
    """
    Real Name: Result System Risk to Human Health
    Original Eqn: Bioretention Risk to Human Health+Bioswale Risk to Human Health+Green Roof Risk to Human Health\\ +GWS Risk to Human Health+LM Risk to Human Health+MBR Risk to Human Health+Porous Pavement Risk to Human Health\\ +RWH Risk to Human Health+SWP Risk to Human Health+SWTW Risk to Human Health+WP Risk to Human Health\\ +WTW Risk to Human Health+WWP Risk to Human Health+WWTW Risk to Human Health
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return bioretention_risk_to_human_health() + bioswale_risk_to_human_health(
    ) + green_roof_risk_to_human_health() + gws_risk_to_human_health() + lm_risk_to_human_health(
    ) + mbr_risk_to_human_health() + porous_pavement_risk_to_human_health(
    ) + rwh_risk_to_human_health() + swp_risk_to_human_health() + swtw_risk_to_human_health(
    ) + wp_risk_to_human_health() + wtw_risk_to_human_health() + wwp_risk_to_human_health(
    ) + wwtw_risk_to_human_health()


@cache('run')
def wwcs_unit_maintenance_energy_m2():
    """
    Real Name: WWCS Unit Maintenance Energy M2
    Original Eqn: 0.05
    Units: KWh/m
    Limits: (None, None)
    Type: constant


    """
    return 0.05


@cache('run')
def ob_lower_vc():
    """
    Real Name: OB Lower VC
    Original Eqn: 0.81
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.81


@cache('run')
def wsc_annual_maintenance():
    """
    Real Name: WSC Annual Maintenance
    Original Eqn: 0.5
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 0.5


@cache('run')
def porous_pavement_risk_to_human_health():
    """
    Real Name: Porous Pavement Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 0.5
    Units: Day
    Limits: (0.0, None)
    Type: constant

    The time step for the simulation.
    """
    return 0.5


@cache('step')
def wp_daily_costs():
    """
    Real Name: WP Daily Costs
    Original Eqn: (WP Unit Conversion Factor * WP Total Dynamic Head of Pump * WP Duration of Pump Operation\\ * WP Price per kWh * (Distributed Treated Water * 0.0115741)) / (WP Motor Efficiency* WP Pump Efficiency*WP Variable Speed Drive Efficiency) + WP Daily Maintenance
    Units: $/Day
    Limits: (None, None)
    Type: component

    Calculating Energy Costs, Chapter 10.8, page 439 Advanced Water Distribution Modeling\t\t0.0115741 is m3/day into l/s
    """
    return (wp_unit_conversion_factor() * wp_total_dynamic_head_of_pump() *
            wp_duration_of_pump_operation() * wp_price_per_kwh() *
            (distributed_treated_water() * 0.0115741)) / (
                wp_motor_efficiency() * wp_pump_efficiency() *
                wp_variable_speed_drive_efficiency()) + wp_daily_maintenance()


@cache('step')
def wwtw_total_ferric_chloride():
    """
    Real Name: WWTW Total Ferric Chloride
    Original Eqn: INTEG ( Treated Wastewater*WWTW Unit Ferric Chloride, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wwtw_total_ferric_chloride()


@cache('run')
def wtw_unit_alum_ghg():
    """
    Real Name: WTW Unit Alum GHG
    Original Eqn: 0.49
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant

    Total GHG Emissions as kgCO2Eq
    """
    return 0.49


@cache('step')
def treated_wastewater():
    """
    Real Name: Treated Wastewater
    Original Eqn: Wastewater Treated
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return wastewater_treated()


@cache('step')
def wwtw_running_costs():
    """
    Real Name: WWTW Running Costs
    Original Eqn: WWTW Administration Costs+WWTW Daily Maintenance+WWTW Staff Costs+(WWTW Electricity for treatment of m3 *Electricity Fee*Treated Wastewater) + (WWTW Sludge Generated*WWTW Sludge Transport and Disposal\\ *Treated Wastewater)
    Units: $/Day
    Limits: (None, None)
    Type: component

    Total Daily Costs of Operation, Maintenance for WWTW ( DODATI U JEDNACINU \n    \t\tI KOLICINU OTPADNE VODE KOJA DOLAZI U POSTROJENJE)
    """
    return wwtw_administration_costs() + wwtw_daily_maintenance() + wwtw_staff_costs() + (
        wwtw_electricity_for_treatment_of_m3() * electricity_fee() * treated_wastewater()) + (
            wwtw_sludge_generated() * wwtw_sludge_transport_and_disposal() * treated_wastewater())


@cache('step')
def rr_total_ghg_ammonium_nitrate():
    """
    Real Name: RR Total GHG Ammonium Nitrate
    Original Eqn: RR Total Ammonium Nitrate Generated*RR Unit GHG Ammonium Nitrate
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return rr_total_ammonium_nitrate_generated() * rr_unit_ghg_ammonium_nitrate()


@cache('step')
def wtw_total_calcium_hydroxide():
    """
    Real Name: WTW Total Calcium Hydroxide
    Original Eqn: INTEG ( Treated Water*WTW Unit Calcium Hydroxide, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_total_calcium_hydroxide()


integ_pp_lcc = functions.Integ(lambda: pp_daily_costs(),
                               lambda: pp_design_and_capital_costs() * pp_footprint())


@cache('run')
def wtw_unit_sodium_hypochlorite_emenergy():
    """
    Real Name: WTW Unit Sodium Hypochlorite EmEnergy
    Original Eqn: 6
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 6


@cache('run')
def wwtw_unit_nitric_acid_emenergy():
    """
    Real Name: WWTW Unit Nitric Acid EmEnergy
    Original Eqn: 3.31
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 3.31


@cache('step')
def gws_tank_inflow():
    """
    Real Name: GWS Tank Inflow
    Original Eqn: (((MF Bathtub Demand * MF WEC Bathtub + MF Clothes Washer Demand * MF WEC Clothes Washer\\ + MF Dishwasher Demand * MF WEC Dishwasher + MF Faucet Demand * MF WEC Faucet)*MF Average Occupancy per Unit *MF Stock of Units) + ((SF Bathtub Demand * SF WEC Bathtub + SF Clothes Washer Demand\\ * SF WEC Clothes Washer + SF Dishwasher Demand * SF WEC Dishwasher + SF Faucet Demand * SF WEC Faucet)*SF Average Occupancy per Unit\\ *SF Stock of Units ))*GWS Percentage of System Coverage *0.001*MF Coefficient of Seasonal Variation
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return (
        ((mf_bathtub_demand() * mf_wec_bathtub() +
          mf_clothes_washer_demand() * mf_wec_clothes_washer() +
          mf_dishwasher_demand() * mf_wec_dishwasher() + mf_faucet_demand() * mf_wec_faucet()) *
         mf_average_occupancy_per_unit() * mf_stock_of_units()) +
        ((sf_bathtub_demand() * sf_wec_bathtub() +
          sf_clothes_washer_demand() * sf_wec_clothes_washer() +
          sf_dishwasher_demand() * sf_wec_dishwasher() + sf_faucet_demand() * sf_wec_faucet()) *
         sf_average_occupancy_per_unit() * sf_stock_of_units())
    ) * gws_percentage_of_system_coverage() * 0.001 * mf_coefficient_of_seasonal_variation()


@cache('run')
def swtw_unit_ferric_chloride_emenergy():
    """
    Real Name: SWTW Unit Ferric Chloride EmEnergy
    Original Eqn: 1.39
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 1.39


@cache('run')
def gws_number_of_tanks():
    """
    Real Name: GWS Number of Tanks
    Original Eqn: 3
    Units: Number
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('step')
def green_roof_total_construction_ghg():
    """
    Real Name: Green Roof Total Construction GHG
    Original Eqn: Green Roof Construction GHG * Green Roof Footprint
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return green_roof_construction_ghg() * green_roof_footprint()


@cache('run')
def unit_demand_per_seat():
    """
    Real Name: Unit Demand per Seat
    Original Eqn: 91.6
    Units: L/Day/Seat
    Limits: (None, None)
    Type: constant

    Source: Water Resources Engineering, Larry W Mays, 2001 (Table 11.1.4. \n    \t\tPage 346)
    """
    return 91.6


@cache('run')
def ia_standard_roof_footprint():
    """
    Real Name: IA Standard Roof Footprint
    Original Eqn: 10000
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 10000


@cache('run')
def full_load_water_use():
    """
    Real Name: Full Load Water Use
    Original Eqn: 1200
    Units: m3/Day
    Limits: (None, None)
    Type: constant


    """
    return 1200


integ_swcs_lc_embodied_ghg = functions.Integ(
    lambda: swcs_maintenance_ghg(),
    lambda: swcs_construction_ghg_m1() + swcs_construction_ghg_m2())


integ_wwtw_embodied_energy_for_chemicals = functions.Integ(lambda: wwtw_total_calcium_hydroxide_emenergy()+wwtw_total_ethanol_emenergy()+wwtw_total_ferric_chloride_emenergy()+wwtw_total_ferric_sulphate_emenergy()+wwtw_total_methanol_emenergy()+wwtw_total_nitric_acid_emenergy(), lambda: 0)


@cache('run')
def wwcs_unit_maintenance_energy_m1():
    """
    Real Name: WWCS Unit Maintenance Energy M1
    Original Eqn: 0.05
    Units: KWh/m
    Limits: (None, None)
    Type: constant

    Energy Report, Table 2.3
    """
    return 0.05


@cache('run')
def ghg_emission_generation_electricity_factor():
    """
    Real Name: GHG Emission Generation Electricity Factor
    Original Eqn: 0.348
    Units: kgCO2/KWh
    Limits: (None, None)
    Type: constant


    """
    return 0.348


@cache('run')
def daycares_lower_vc():
    """
    Real Name: Daycares Lower VC
    Original Eqn: 1.14
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1.14


@cache('step')
def hvac_demand_variation_coefficient():
    """
    Real Name: HVAC Demand Variation Coefficient
    Original Eqn: WITH LOOKUP ( Months, ([(0,0)-(12,10)],(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1\\ ),(12,1) ))
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(months(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])


@cache('run')
def swp_pump_efficiency():
    """
    Real Name: SWP Pump Efficiency
    Original Eqn: 93
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Pump Efficiency [%]
    """
    return 93


@cache('run')
def wtw_unit_calcium_hydroxide_emenergy():
    """
    Real Name: WTW Unit Calcium Hydroxide EmEnergy
    Original Eqn: 1
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('run')
def unit_industrial_demand_per_floor_area():
    """
    Real Name: Unit Industrial Demand Per Floor Area
    Original Eqn: 180
    Units: L/(m2*Day)
    Limits: (None, None)
    Type: constant

    180000 L/Floor m2/day\t\tOvde je 180 L/m2*Day
    """
    return 180


@cache('step')
def dem_daycares():
    """
    Real Name: Dem Daycares
    Original Eqn: Daycares Demand Variation Coefficient*Number of Children*Unit Demand per Child
    Units: L/Day
    Limits: (None, None)
    Type: component


    """
    return daycares_demand_variation_coefficient() * number_of_children() * unit_demand_per_child()


@cache('run')
def lm_percentage_of_ob():
    """
    Real Name: LM Percentage of OB
    Original Eqn: 0.65
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Percentage of OB area used to collect black water
    """
    return 0.65


@cache('step')
def dem_restaurants():
    """
    Real Name: Dem Restaurants
    Original Eqn: Restaurant Seats * Unit Demand per Seat * Restaurants Demand Variation Coefficient
    Units: L/Day
    Limits: (None, None)
    Type: component

    Source: Water Resources Engineering, Larry W Mays, 2001 (Table 11.1.4. Page 346)\t\tWater Distribution System Design PPT
    """
    return restaurant_seats() * unit_demand_per_seat() * restaurants_demand_variation_coefficient()


@cache('run')
def rr_unit_ghg_ammonium_nitrate():
    """
    Real Name: RR Unit GHG Ammonium Nitrate
    Original Eqn: 2.97
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 2.97


@cache('run')
def green_roof_risk_to_human_health():
    """
    Real Name: Green Roof Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def swt_unit_ferric_chloride_ghg():
    """
    Real Name: SWT Unit Ferric Chloride GHG
    Original Eqn: 0.26
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.26


@cache('step')
def wtw_total_sodium_hypochlorite():
    """
    Real Name: WTW Total Sodium Hypochlorite
    Original Eqn: INTEG ( Treated Water*WTW Unit Sodium Hypochlorite, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_total_sodium_hypochlorite()


@cache('run')
def wtw_space_requirements():
    """
    Real Name: WTW Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


integ_green_roof_lcc = functions.Integ(
    lambda: green_roof_daily_costs(),
    lambda: green_roof_design_and_capital_costs() * green_roof_footprint())

integ_ia_runoff_total = functions.Integ(lambda: ia_runoff_daily(), lambda: 0)


@cache('step')
def wwcs_running_costs():
    """
    Real Name: WWCS Running Costs
    Original Eqn: WWCS Daily Maintenance
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return wwcs_daily_maintenance()


@cache('run')
def green_roof_flexibility_and_adaptability():
    """
    Real Name: Green Roof Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def rb_and_cistern_percentage():
    """
    Real Name: RB and Cistern Percentage
    Original Eqn: (100*RB and Cistern Footprint)/LU Sum
    Units: Percentage
    Limits: (None, None)
    Type: component


    """
    return (100 * rb_and_cistern_footprint()) / lu_sum()


@cache('run')
def rb_and_cistern_storage_volume():
    """
    Real Name: RB and Cistern Storage Volume
    Original Eqn: 400
    Units: m3
    Limits: (None, None)
    Type: constant

    Table 4.1.3: Recommended rainwater storage tank capacities for various catchment \n    \t\tareas and water demands for systems in Toronto\t\tPage 4.16
    """
    return 400


@cache('step')
def rb_and_cistern_daily_costs():
    """
    Real Name: RB and Cistern Daily Costs
    Original Eqn: (RB and Cistern Storage Volume * RB and Cistern Annual Maintenance Costs)/365.25
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return (rb_and_cistern_storage_volume() * rb_and_cistern_annual_maintenance_costs()) / 365.25


@cache('run')
def gws_plumbing_costs_per_m2():
    """
    Real Name: GWS Plumbing Costs per m2
    Original Eqn: 1250
    Units: $/m2
    Limits: (None, None)
    Type: constant

    http://onetorontoplumbing.com/2015/what-can-you-expect-to-pay-for-drain-pipe-lining-i\n    \t\tn-toronto/\t\tCompare that to 3000\u2019 of pipe in a high rise condominium, it could be \n    \t\t$125 per foot.
    """
    return 1250


@cache('step')
def rhp_total_lcc():
    """
    Real Name: RHP Total LCC
    Original Eqn: INTEG ( RHP Daily Costs, (RHP Construction and Installation)*RHP Number of Pumps)
    Units: $
    Limits: (None, None)
    Type: component

    Costs of Pumping Station Installation
    """
    return integ_rhp_total_lcc()


@cache('run')
def wwtw_daily_treatment_capacity():
    """
    Real Name: WWTW Daily Treatment Capacity
    Original Eqn: 10000
    Units: m3/Day
    Limits: (None, None)
    Type: constant

    Capacity of Wastewater treatment plant in Cubic Meters per day
    """
    return 10000


@cache('run')
def pp_annual_maintenance_costs():
    """
    Real Name: PP Annual Maintenance Costs
    Original Eqn: 120
    Units: $/m2
    Limits: (None, None)
    Type: constant


    """
    return 120


@cache('step')
def rh_tank_inflow():
    """
    Real Name: RH Tank Inflow
    Original Eqn: (Green Roof Runoff Daily + (IA Runoff Daily * IA Percentage of Area Collected)) * RH Control
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return (green_roof_runoff_daily() +
            (ia_runoff_daily() * ia_percentage_of_area_collected())) * rh_control()


@cache('run')
def wwcs_unit_construction_ghg_m2():
    """
    Real Name: WWCS Unit Construction GHG M2
    Original Eqn: 2.36
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 2.36


@cache('run')
def wwcs_unit_construction_ghg_m1():
    """
    Real Name: WWCS Unit Construction GHG M1
    Original Eqn: 2.36
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant

    GHG Emissions per kg of Pipe Materials, Appendix A
    """
    return 2.36


@cache('run')
def rr_unit_emenergy_ammonium_nitrate():
    """
    Real Name: RR Unit EmEnergy Ammonium Nitrate
    Original Eqn: 2.72
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 2.72


@cache('run')
def bioswale_annual_maintenance_costs():
    """
    Real Name: Bioswale Annual Maintenance Costs
    Original Eqn: 250
    Units: $/m2
    Limits: (None, None)
    Type: constant


    """
    return 250


@cache('step')
def mf_units_decomissioned():
    """
    Real Name: MF Units Decomissioned
    Original Eqn: INTEGER( MF Decommissioned Units Annually / Days in a Year)
    Units: MF Units/Day
    Limits: (None, None)
    Type: component


    """
    return int(mf_decommissioned_units_annually() / days_in_a_year())


@cache('run')
def green_roof_reliability():
    """
    Real Name: Green Roof Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('step')
def wtw_total_costs():
    """
    Real Name: WTW Total Costs
    Original Eqn: INTEG ( WTW Running Costs, (WTW Construction and Installation + WTW Capital Investment)*1e+006)
    Units: $
    Limits: (None, None)
    Type: component

    Total Costs for Water Treatment Works
    """
    return integ_wtw_total_costs()


integ_mbr_total_lcc = functions.Integ(
    lambda: mbr_daily_maintenance(),
    lambda: mbr_installation_and_construction_costs() * mbr_number_of_mbr())


@cache('step')
def wtw_total_alum_emenergy():
    """
    Real Name: WTW Total Alum EmEnergy
    Original Eqn: WTW Total Alum*WTW Unit Alum EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component

    Total Embodied Energy Required for Alum use in Water Treatment
    """
    return wtw_total_alum() * wtw_unit_alum_emenergy()


@cache('step')
def mf_stock_of_water_sensitive_units():
    """
    Real Name: MF Stock of Water Sensitive Units
    Original Eqn: MF Rate of Adoption * MF Stock of Units
    Units: MF Units
    Limits: (None, None)
    Type: component


    """
    return mf_rate_of_adoption() * mf_stock_of_units()


@cache('step')
def ia_runoff_total():
    """
    Real Name: IA Runoff Total
    Original Eqn: INTEG ( IA Runoff Daily, 0)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return integ_ia_runoff_total()


@cache('run')
def lm_percentage_of_schools():
    """
    Real Name: LM Percentage of Schools
    Original Eqn: 0.88
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.88


@cache('step')
def landuse1_nitrogen():
    """
    Real Name: Landuse1 Nitrogen
    Original Eqn: INTEG ( Landuse1 Daily Nitrogen, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_landuse1_nitrogen()


@cache('step')
def gwp_daily_costs():
    """
    Real Name: GWP Daily Costs
    Original Eqn: (((GWP Unit Conversion Factor * GWP Average Dynamic Head * GWP Duration of Pump Operation\\ * WP Price per kWh * GWS Tank Outflow * 0.0115741) / (GWP Motor Efficiency*GWP Pump Efficiency*GWP Variable Speed Drive Efficiency\\ )) + GWP Daily Maintenance)*GWP Number of Pumps
    Units: $/Day
    Limits: (None, None)
    Type: component

    Calculating Energy Costs, Chapter 10.8, page 439 Advanced Water Distribution Modeling\t\t* 0.0115741 Conversion Factor m3/day l/s
    """
    return ((
        (gwp_unit_conversion_factor() * gwp_average_dynamic_head() *
         gwp_duration_of_pump_operation() * wp_price_per_kwh() * gws_tank_outflow() * 0.0115741) /
        (gwp_motor_efficiency() * gwp_pump_efficiency() * gwp_variable_speed_drive_efficiency())) +
            gwp_daily_maintenance()) * gwp_number_of_pumps()


@cache('step')
def rainfall():
    """
    Real Name: Rainfall
    Original Eqn: INTEGER( RANDOM UNIFORM( 1, 150, 1 ) )
    Units: mm
    Limits: (None, None)
    Type: component


    """
    return int(functions.random_uniform(1, 150, 1))


@cache('run')
def wdm_replacement():
    """
    Real Name: WDM Replacement
    Original Eqn: 0
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def bioswale_footprint():
    """
    Real Name: Bioswale Footprint
    Original Eqn: 0
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def wwtw_total_nitric_acid_ghg():
    """
    Real Name: WWTW Total Nitric Acid GHG
    Original Eqn: WWTW Total Nitric Acid*WWTW Unit Nitric Acid GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_nitric_acid() * wwtw_unit_nitric_acid_ghg()


@cache('run')
def landuse4():
    """
    Real Name: Landuse4
    Original Eqn: 0
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def landuse2_emc_nitrogen():
    """
    Real Name: Landuse2 EMC Nitrogen
    Original Eqn: 1.2
    Units: mg/L
    Limits: (0.4, 5.5, 0.1)
    Type: constant

    LTHIA-LID EMC Concetration Value Matrix for Commercila, Industrial, \n    \t\tResidential, Grass pasture, Agriculture, Forest
    """
    return 1.2


@cache('run')
def landuse1():
    """
    Real Name: Landuse1
    Original Eqn: 20000
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 20000


@cache('run')
def swp_annual_maintenance():
    """
    Real Name: SWP Annual Maintenance
    Original Eqn: 10000
    Units: $
    Limits: (None, None)
    Type: constant

    Percentage of Initial Costs
    """
    return 10000


@cache('run')
def landuse3():
    """
    Real Name: Landuse3
    Original Eqn: 10000
    Units: mm
    Limits: (None, None)
    Type: constant


    """
    return 10000


integ_swcs_total_costs = functions.Integ(
    lambda: swcs_running_costs(),
    lambda: swcs_construction() + swcs_replacement() + swcs_disposal())


@cache('step')
def ia_runoff_daily():
    """
    Real Name: IA Runoff Daily
    Original Eqn: (Rainfall * IA Runoff Coefficient * (IA Roads and Sidewalks Footprint+IA Standard Roof Footprint\\ +IA Parking Footprint))*0.001
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return (rainfall() * ia_runoff_coefficient() *
            (ia_roads_and_sidewalks_footprint() + ia_standard_roof_footprint() +
             ia_parking_footprint())) * 0.001


@cache('step')
def pp_lcc():
    """
    Real Name: PP LCC
    Original Eqn: INTEG ( PP Daily Costs, PP Design and Capital Costs * PP Footprint)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_pp_lcc()


@cache('step')
def wwcs_total_weight_m2():
    """
    Real Name: WWCS Total Weight M2
    Original Eqn: WWCS Total Length M2*WWCS Unit Weight M2
    Units: kg
    Limits: (None, None)
    Type: component

    Weight in Killograms for Material 2
    """
    return wwcs_total_length_m2() * wwcs_unit_weight_m2()


@cache('step')
def wdm_daily_maintenance_costs():
    """
    Real Name: WDM Daily Maintenance Costs
    Original Eqn: WDM Annual Maintenance / 365.25
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return wdm_annual_maintenance() / 365.25


@cache('step')
def wwcs_total_weight_m1():
    """
    Real Name: WWCS Total Weight M1
    Original Eqn: WWCS Total Length M1*WWCS Unit Weight M1
    Units: kg
    Limits: (None, None)
    Type: component

    Total Weight of Stormwater System (in Killograms)
    """
    return wwcs_total_length_m1() * wwcs_unit_weight_m1()


@cache('step')
def wtw_administration_costs():
    """
    Real Name: WTW Administration Costs
    Original Eqn: WTW Administration Rate*WTW Staff Costs
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return wtw_administration_rate() * wtw_staff_costs()


@cache('step')
def bioretention_percentage():
    """
    Real Name: Bioretention Percentage
    Original Eqn: (100*Bioretention Footprint)/LU Sum
    Units: Percentage
    Limits: (None, None)
    Type: component


    """
    return (100 * bioretention_footprint()) / lu_sum()


@cache('run')
def dem_ob_restroom():
    """
    Real Name: Dem OB Restroom
    Original Eqn: 0.32
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.32


@cache('step')
def mbr_daily_ghg_emission():
    """
    Real Name: MBR Daily GHG Emission
    Original Eqn: MBR GHG per m3
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return mbr_ghg_per_m3()


@cache('run')
def wwtw_unit_calcium_hydroxide_emenergy():
    """
    Real Name: WWTW Unit Calcium Hydroxide EmEnergy
    Original Eqn: 1
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def wwtw_operation_electricity():
    """
    Real Name: WWTW Operation Electricity
    Original Eqn: INTEG ( WWTW Treated Wastewater*WWTW Electricity for treatment of m3, 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_wwtw_operation_electricity()


@cache('run')
def cc_area():
    """
    Real Name: CC Area
    Original Eqn: 3500
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 3500


@cache('run')
def swcs_unit_construction_energy_m2():
    """
    Real Name: SWCS Unit Construction Energy M2
    Original Eqn: 0.9
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.9


@cache('run')
def swcs_unit_construction_energy_m1():
    """
    Real Name: SWCS Unit Construction Energy M1
    Original Eqn: 0.9
    Units: KWh/kg
    Limits: (None, None)
    Type: constant

    Embodied Energy for different categories of materials used for Stormwater \n    \t\tSystem. Table Appendix A WaterMet2
    """
    return 0.9


@cache('run')
def sf_faucet_demand():
    """
    Real Name: SF Faucet Demand
    Original Eqn: 29
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 29


@cache('run')
def sf_average_lot_size():
    """
    Real Name: SF Average Lot Size
    Original Eqn: 1000
    Units: m2
    Limits: (None, None)
    Type: constant

    Average size of a single family lot in square meters
    """
    return 1000


@cache('step')
def rh_total_water_harvested():
    """
    Real Name: RH Total Water Harvested
    Original Eqn: INTEG ( RH Tank Inflow, 0)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return integ_rh_total_water_harvested()


@cache('run')
def wtw_unit_microsand():
    """
    Real Name: WTW Unit Microsand
    Original Eqn: 0.00308
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.00308


@cache('step')
def result_network_embodied_ghg_emissions():
    """
    Real Name: Result Network Embodied GHG Emissions
    Original Eqn: SWCS LC Embodied GHG + WDM LC Embodied GHG + WWCS LC Embodied GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return swcs_lc_embodied_ghg() + wdm_lc_embodied_ghg() + wwcs_lc_embodied_ghg()


@cache('step')
def wwtw_total_ethanol_emenergy():
    """
    Real Name: WWTW Total Ethanol EmEnergy
    Original Eqn: WWTW Total Ethanol*WWTW Unit Ethanol EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_ethanol() * wwtw_unit_ethanol_emenergy()


integ_wwcs_total_costs = functions.Integ(
    lambda: wwcs_running_costs(),
    lambda: wwcs_construction() + wwcs_replacement() + wwcs_disposal())


@cache('step')
def wwtw_total_ethanol_ghg():
    """
    Real Name: WWTW Total Ethanol GHG
    Original Eqn: WWTW Total Ethanol*WWTW Unit Ethanol GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_ethanol() * wwtw_unit_ethanol_ghg()


@cache('step')
def lm_daily_treated():
    """
    Real Name: LM Daily Treated
    Original Eqn: LM Inflow Total
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return lm_inflow_total()


integ_wdm_lc_embodied_ghg = functions.Integ(
    lambda: wdm_maintenance_ghg(), lambda: wdm_construction_ghg_m1() + wdm_construction_ghg_m2())


@cache('run')
def gws_affordability():
    """
    Real Name: GWS Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('run')
def mbr_ghg_per_m3():
    """
    Real Name: MBR GHG per m3
    Original Eqn: 18
    Units: kgCO2eq/m3
    Limits: (None, None)
    Type: constant

    Figure 3. LCA results for the decentralized LM treatment and water reuse \n    \t\tsystem. (a) Annualized results for the analysis period (25 years) for the \n    \t\tentire system per ML of influent that is treated and recycled.
    """
    return 18


@cache('run')
def gws_installation_costs():
    """
    Real Name: GWS Installation Costs
    Original Eqn: 2000
    Units: $/m3
    Limits: (None, None)
    Type: constant

    Using Graywater and Stormwater to Enhance Local Water Supplies: An Assessment of \n    \t\tRisks, Costs, and Benefits\t\tTable 7.1 Cost of Graywater Treatment and Storage Systems of Varying Scale, \n    \t\tIncluding a Coarse Filter and Chlorine Disinfection\t\tSystem
    """
    return 2000


@cache('step')
def wtw_operation_daily_energy():
    """
    Real Name: WTW Operation Daily Energy
    Original Eqn: Distributed Treated Water * WTW Electricity for treatment of m3
    Units: KWh/Day
    Limits: (None, None)
    Type: component


    """
    return distributed_treated_water() * wtw_electricity_for_treatment_of_m3()


@cache('run')
def mf_wec_bathtub():
    """
    Real Name: MF WEC Bathtub
    Original Eqn: 1
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Water Efficiency Coefficient - Random
    """
    return 1


@cache('step')
def lm_total_lcc():
    """
    Real Name: LM Total LCC
    Original Eqn: INTEG ( LM Daily Maintenance, LM Installation and Construction * LN Number of LM)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_lm_total_lcc()


@cache('step')
def sf_units_total_area_occupied():
    """
    Real Name: SF Units Total Area Occupied
    Original Eqn: SF Stock of Units*SF Average Lot Size
    Units: m2
    Limits: (None, None)
    Type: component


    """
    return sf_stock_of_units() * sf_average_lot_size()


@cache('step')
def swcs_running_costs():
    """
    Real Name: SWCS Running Costs
    Original Eqn: SWCS Daily Maintenance
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return swcs_daily_maintenance()


@cache('run')
def wwp_unit_conversion_factor():
    """
    Real Name: WWP Unit Conversion Factor
    Original Eqn: 101.9
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 101.9


@cache('step')
def wwtw_staff_costs():
    """
    Real Name: WWTW Staff Costs
    Original Eqn: (WWTW Average Salary*WWTW Number of Staff)/Days in a Year
    Units: $/Day
    Limits: (None, None)
    Type: component

    Staff costs on a daily scale (annual salary divided by 365)
    """
    return (wwtw_average_salary() * wwtw_number_of_staff()) / days_in_a_year()


@cache('step')
def domestic_demand():
    """
    Real Name: Domestic Demand
    Original Eqn: (((MF Average Occupancy per Unit * MF Stock of No Measure Units * MF WD per Capita No Measures\\ )+(MF Average Occupancy per Unit * MF WD per Capita Water Sensitive * MF Stock of Water Sensitive Units))+((SF Average Occupancy per Unit\\ * SF Stock of No Measure Units * SF WD per Capita No Measures + SF Average Occupancy per Unit * SF Stock of Water Sensitive Units\\ * SF WD per Capita Water Sensitive))) * 0.001
    Units: m3/Day
    Limits: (None, None)
    Type: component

    Total Domestic Daily Water Demand in Cubic Meters = Single Family + Multi \n    \t\tFamily Including the use of water sensitive appliances
    """
    return (((mf_average_occupancy_per_unit() * mf_stock_of_no_measure_units() *
              mf_wd_per_capita_no_measures()) +
             (mf_average_occupancy_per_unit() * mf_wd_per_capita_water_sensitive() *
              mf_stock_of_water_sensitive_units())) +
            ((sf_average_occupancy_per_unit() * sf_stock_of_no_measure_units() *
              sf_wd_per_capita_no_measures() + sf_average_occupancy_per_unit() *
              sf_stock_of_water_sensitive_units() * sf_wd_per_capita_water_sensitive()))) * 0.001


@cache('step')
def result_network_embodied_energy():
    """
    Real Name: Result Network Embodied Energy
    Original Eqn: SWCS LC Energy Embodied+WDM LC Embodied Energy+WWCS LC Embodied Energy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return swcs_lc_energy_embodied() + wdm_lc_embodied_energy() + wwcs_lc_embodied_energy()


integ_wtw_total_carbon_dioxide = functions.Integ(
    lambda: treated_water() * wtw_unit_carbon_dioxide(), lambda: 0)

integ_rh_tank_current_storage_volume = functions.Integ(
    lambda: rh_tank_inflow() - rh_tank_outflow(), lambda: 0)

integ_wwtw_total_ethanol = functions.Integ(lambda: treated_wastewater() * wwtw_unit_ethanol(),
                                           lambda: 0)


@cache('step')
def rr_total_emenergy_ammonium_nitrate():
    """
    Real Name: RR Total EmEnergy Ammonium Nitrate
    Original Eqn: RR Total Ammonium Nitrate Generated*RR Unit EmEnergy Ammonium Nitrate
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return rr_total_ammonium_nitrate_generated() * rr_unit_emenergy_ammonium_nitrate()


@cache('step')
def wtw_staff_costs():
    """
    Real Name: WTW Staff Costs
    Original Eqn: (WTW Average Staff Salary*WTW Number of Staff)/Days in a Year
    Units: $
    Limits: (None, None)
    Type: component

    Daily WTW Staff Costs
    """
    return (wtw_average_staff_salary() * wtw_number_of_staff()) / days_in_a_year()


integ_lm_total_treated = functions.Integ(lambda: lm_daily_treated(), lambda: 0)


@cache('run')
def gws_acceptability():
    """
    Real Name: GWS Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def wdm_unit_maintenance_energy_m2():
    """
    Real Name: WDM Unit Maintenance Energy M2
    Original Eqn: 0.05
    Units: KWh/m
    Limits: (None, None)
    Type: constant


    """
    return 0.05


integ_wtw_total_sodium_hypochlorite = functions.Integ(
    lambda: treated_water() * wtw_unit_sodium_hypochlorite(), lambda: 0)


@cache('run')
def wwtw_available_capacity():
    """
    Real Name: WWTW Available Capacity
    Original Eqn: 0.95
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.95


@cache('run')
def green_roof_annual_maintenance_costs():
    """
    Real Name: Green Roof Annual Maintenance Costs
    Original Eqn: 500
    Units: $/m2
    Limits: (None, None)
    Type: constant


    """
    return 500


@cache('run')
def bioretention_reliability():
    """
    Real Name: Bioretention Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('step')
def mbr_total_ghg_emission():
    """
    Real Name: MBR Total GHG Emission
    Original Eqn: INTEG ( MBR Daily GHG Emission, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_mbr_total_ghg_emission()


@cache('step')
def wdm_emenergy_maintenance():
    """
    Real Name: WDM EmEnergy Maintenance
    Original Eqn: ((WDM Total Length M1*WDM Unit Maintenance Energy M1)+(WDM Unit Maintenance Energy M2\\ *WDM Total Length M2))*WDM Number of Maintenance Trips
    Units: KWh/Day
    Limits: (None, None)
    Type: component


    """
    return ((wdm_total_length_m1() * wdm_unit_maintenance_energy_m1()) +
            (wdm_unit_maintenance_energy_m2() * wdm_total_length_m2())
            ) * wdm_number_of_maintenance_trips()


@cache('step')
def rhp_daily_maintenance():
    """
    Real Name: RHP Daily Maintenance
    Original Eqn: RHP Annual Maintenance/Days in a Year
    Units: $
    Limits: (None, None)
    Type: component


    """
    return rhp_annual_maintenance() / days_in_a_year()


@cache('step')
def mbr_total_energy():
    """
    Real Name: MBR Total Energy
    Original Eqn: INTEG ( -MBR Daily Energy Consumption, 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_mbr_total_energy()


@cache('step')
def swcs_construction_ghg_m1():
    """
    Real Name: SWCS Construction GHG M1
    Original Eqn: SWCS Total Weight M1*SWCS Unit Construction GHG M1
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return swcs_total_weight_m1() * swcs_unit_construction_ghg_m1()


@cache('run')
def number_of_children():
    """
    Real Name: Number of Children
    Original Eqn: 550
    Units: Persons
    Limits: (None, None)
    Type: constant


    """
    return 550


@cache('run')
def wp_acceptability():
    """
    Real Name: WP Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (1.0, 5.0, 1.0)
    Type: constant


    """
    return 3


@cache('run')
def bioswale_contruction_ghg():
    """
    Real Name: Bioswale Contruction GHG
    Original Eqn: 0.021
    Units: kgCO2eq/m2
    Limits: (None, None)
    Type: constant

    Table 2.3 Energy Consumption and CO2 Emissions Indicators for Drainage \n    \t\tSystem Construction and Maintenance
    """
    return 0.021


@cache('run')
def wp_duration_of_pump_operation():
    """
    Real Name: WP Duration of Pump Operation
    Original Eqn: 12
    Units: Hours
    Limits: (None, None)
    Type: constant

    Number of Hours for Pump Operations (Assumption is 24 hours)
    """
    return 12


@cache('step')
def sf_wd_per_capita_water_sensitive():
    """
    Real Name: SF WD per Capita Water Sensitive
    Original Eqn: (SF Bathtub Demand * SF WEC Bathtub + SF Clothes Washer Demand * SF WEC Clothes Washer\\ + SF Dishwasher Demand * SF WEC Dishwasher + SF Faucet Demand * SF WEC Faucet + SF Leaks\\ * SF WEC Leaks + SF Shower Demand * SF WEC Shower + SF Toilet Demand * SF WEC Toilet\\ + SF Other) * MF Coefficient of Seasonal Variation
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: component


    """
    return (sf_bathtub_demand() * sf_wec_bathtub() + sf_clothes_washer_demand() *
            sf_wec_clothes_washer() + sf_dishwasher_demand() * sf_wec_dishwasher() +
            sf_faucet_demand() * sf_wec_faucet() + sf_leaks() * sf_wec_leaks() +
            sf_shower_demand() * sf_wec_shower() + sf_toilet_demand() * sf_wec_toilet() +
            sf_other()) * mf_coefficient_of_seasonal_variation()


@cache('run')
def ob_upper_vc():
    """
    Real Name: OB Upper VC
    Original Eqn: 1.17
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1.17


@cache('step')
def lm_total_treated():
    """
    Real Name: LM Total Treated
    Original Eqn: INTEG ( LM Daily Treated, 0)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return integ_lm_total_treated()


@cache('run')
def wp_co2_per_kwh():
    """
    Real Name: WP CO2 per kWh
    Original Eqn: 0.05
    Units: kgCO2/KWh
    Limits: (None, None)
    Type: constant

    0.05kg (50gr) CO2 per kWh for Ontario, Canada
    """
    return 0.05


@cache('run')
def wp_variable_speed_drive_efficiency():
    """
    Real Name: WP Variable Speed Drive Efficiency
    Original Eqn: 88
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Variable Speed Drive Efficiency [%]
    """
    return 88


@cache('step')
def rr_total_ghg_urea():
    """
    Real Name: RR Total GHG Urea
    Original Eqn: RR Total Urea Generated*RR Unit GHG Urea
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return rr_total_urea_generated() * rr_unit_ghg_urea()


integ_wtw_total_polyaluminium_chloride = functions.Integ(
    lambda: treated_water() * wtw_unit_polyaluminium_chloride(), lambda: 0)


@cache('step')
def bioswale_percentage():
    """
    Real Name: Bioswale Percentage
    Original Eqn: (100*Bioswale Footprint)/LU Sum
    Units: Percentage
    Limits: (None, None)
    Type: component


    """
    return (100 * bioswale_footprint()) / lu_sum()


@cache('step')
def dem_retail():
    """
    Real Name: Dem Retail
    Original Eqn: Retail space in m2*Unit Demand of Retail Space*Retail Demand Variation Coefficient
    Units: L/Day
    Limits: (None, None)
    Type: component


    """
    return retail_space_in_m2() * unit_demand_of_retail_space(
    ) * retail_demand_variation_coefficient()


integ_rb_and_cistern_lcc = functions.Integ(
    lambda: rb_and_cistern_daily_costs(),
    lambda: rb_design_and_capital_costs() * rb_and_cistern_storage_volume())


@cache('run')
def rwh_space_requirements():
    """
    Real Name: RWH Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def wsc_running_costs():
    """
    Real Name: WSC Running Costs
    Original Eqn: WSC Daily Maintenance
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return wsc_daily_maintenance()


@cache('run')
def bioretention_design_and_capital_costs():
    """
    Real Name: Bioretention Design and Capital Costs
    Original Eqn: 250
    Units: $/m2
    Limits: (None, None)
    Type: constant


    """
    return 250


integ_wwtw_total_nitric_acid = functions.Integ(
    lambda: treated_wastewater() * wwtw_unit_nitric_acid(), lambda: 0)


@cache('step')
def rr_biogas_generated():
    """
    Real Name: RR Biogas Generated
    Original Eqn: INTEG ( RR Daily Biogas, 0)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return integ_rr_biogas_generated()


@cache('run')
def wtm_annual_maintenance():
    """
    Real Name: WTM Annual Maintenance
    Original Eqn: 1
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('step')
def pp_total_construction_ghg():
    """
    Real Name: PP Total Construction GHG
    Original Eqn: PP Construction GHG*PP Footprint
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return pp_construction_ghg() * pp_footprint()


@cache('step')
def years():
    """
    Real Name: Years
    Original Eqn: Utility Years + 1
    Units: Year
    Limits: (None, None)
    Type: component


    """
    return utility_years() + 1


@cache('run')
def wtw_unit_polyaluimium_chloride_ghg():
    """
    Real Name: WTW Unit Polyaluimium Chloride GHG
    Original Eqn: 1.14
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 1.14


@cache('step')
def wtw_running_costs():
    """
    Real Name: WTW Running Costs
    Original Eqn: WTW Daily Maintenance + WTW Staff Costs + (WTW Water Resource Fee*Distributed Treated Water\\ )+(Electricity Fee *WTW Electricity for treatment of m3*Distributed Treated Water)+WTW Administration Costs
    Units: $
    Limits: (None, None)
    Type: component


    """
    return wtw_daily_maintenance() + wtw_staff_costs() + (
        wtw_water_resource_fee() * distributed_treated_water()) + (
            electricity_fee() * wtw_electricity_for_treatment_of_m3() *
            distributed_treated_water()) + wtw_administration_costs()


@cache('run')
def bioswale_reliability():
    """
    Real Name: Bioswale Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def wwtw_capital_investment():
    """
    Real Name: WWTW Capital Investment
    Original Eqn: 15.7
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 15.7


@cache('step')
def wwcs_construction_energy_m2():
    """
    Real Name: WWCS Construction Energy M2
    Original Eqn: WWCS Total Weight M2*WWCS Unit Construction Energy M2
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wwcs_total_weight_m2() * wwcs_unit_construction_energy_m2()


integ_wwp_total_ghg_emission = functions.Integ(lambda: wwp_daily_ghg_emissions(), lambda: 0)


@cache('run')
def mbr_annual_maintenance():
    """
    Real Name: MBR Annual Maintenance
    Original Eqn: 15000
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 15000


@cache('run')
def sf_shower_demand():
    """
    Real Name: SF Shower Demand
    Original Eqn: 36
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 36


@cache('run')
def bioswale_acceptability():
    """
    Real Name: Bioswale Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('step')
def result_pumping_ghg_emissions():
    """
    Real Name: Result Pumping GHG Emissions
    Original Eqn: SWP Total GHG Emission+WP Total GHG Emission+WWP Total GHG Emission
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return swp_total_ghg_emission() + wp_total_ghg_emission() + wwp_total_ghg_emission()


@cache('step')
def wtw_reserved_treatment_capacity():
    """
    Real Name: WTW Reserved Treatment Capacity
    Original Eqn: WTW Daily Treatment Capacity * WTW Available Capacity
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return wtw_daily_treatment_capacity() * wtw_available_capacity()


@cache('run')
def sf_toilet_demand():
    """
    Real Name: SF Toilet Demand
    Original Eqn: 53
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 53


@cache('run')
def wp_construction_and_installation():
    """
    Real Name: WP Construction and Installation
    Original Eqn: 150000
    Units: $
    Limits: (None, None)
    Type: constant

    Installation Costs in $
    """
    return 150000


@cache('run')
def swcs_unit_weight_m2():
    """
    Real Name: SWCS Unit Weight M2
    Original Eqn: 10
    Units: kg/m
    Limits: (None, None)
    Type: constant

    Material 2
    """
    return 10


@cache('run')
def swcs_unit_weight_m1():
    """
    Real Name: SWCS Unit Weight M1
    Original Eqn: 10
    Units: kg/m
    Limits: (None, None)
    Type: constant

    Unit Weight of 1m' of Material (PVC, PE, Mild Steel, Concrete, etc)
    """
    return 10


integ_stormwater_tank = functions.Integ(lambda: sw_daily_rate() - sw_release_rate(), lambda: 0)


@cache('run')
def wwtw_unit_calcium_hydroxide():
    """
    Real Name: WWTW Unit Calcium Hydroxide
    Original Eqn: 0.03
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.03


@cache('step')
def weeks():
    """
    Real Name: Weeks
    Original Eqn: (INTEGER (Time/7)) + 1
    Units: Week
    Limits: (None, None)
    Type: component


    """
    return (int(time() / 7)) + 1


@cache('run')
def bioswale_affordability():
    """
    Real Name: Bioswale Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('run')
def rhp_motor_efficiency():
    """
    Real Name: RHP Motor Efficiency
    Original Eqn: 80
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Motor Efficiency [%]
    """
    return 80


@cache('run')
def rr_unit_biogas():
    """
    Real Name: RR Unit Biogas
    Original Eqn: 20
    Units: m3/m3
    Limits: (None, None)
    Type: constant

    Specification of Recovered Resources in Wastewater Tretmant Works
    """
    return 20


@cache('step')
def wdm_construction_ghg_m2():
    """
    Real Name: WDM Construction GHG M2
    Original Eqn: WDM Total Weight M2*WDM Unit Construction GHG M2
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wdm_total_weight_m2() * wdm_unit_construction_ghg_m2()


@cache('run')
def sws_total_length_m1():
    """
    Real Name: SWS Total Length M1
    Original Eqn: 4500
    Units: m
    Limits: (None, None)
    Type: constant

    Length of Stormwater System
    """
    return 4500


@cache('step')
def mbr_daily_maintenance():
    """
    Real Name: MBR Daily Maintenance
    Original Eqn: MBR Annual Maintenance / Days in a Year
    Units: $/Day
    Limits: (None, None)
    Type: component

    Daily Costs of LM Maintenance
    """
    return mbr_annual_maintenance() / days_in_a_year()


@cache('step')
def wdm_construction_ghg_m1():
    """
    Real Name: WDM Construction GHG M1
    Original Eqn: WDM Total Weight M1*WDM Unit Construction GHG M1
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wdm_total_weight_m1() * wdm_unit_construction_ghg_m1()


@cache('run')
def mf_leaks():
    """
    Real Name: MF Leaks
    Original Eqn: 20
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 20


@cache('run')
def mf_toilet_demand():
    """
    Real Name: MF Toilet Demand
    Original Eqn: 53
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 53


@cache('step')
def asphalt_construction_energy():
    """
    Real Name: Asphalt Construction Energy
    Original Eqn: Asphalt Unit Energy * (IA Parking Footprint + IA Roads and Sidewalks Footprint)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return asphalt_unit_energy() * (ia_parking_footprint() + ia_roads_and_sidewalks_footprint())


@cache('run')
def mf_wec_leaks():
    """
    Real Name: MF WEC Leaks
    Original Eqn: 1
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 1


@cache('run')
def mbr_affordability():
    """
    Real Name: MBR Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('run')
def wwtw_unit_methanol_emenergy():
    """
    Real Name: WWTW Unit Methanol EmEnergy
    Original Eqn: 4.56
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 4.56


@cache('run')
def wwcs_unit_construction_energy_m2():
    """
    Real Name: WWCS Unit Construction Energy M2
    Original Eqn: 0.9
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.9


@cache('run')
def rr_unit_urea():
    """
    Real Name: RR Unit Urea
    Original Eqn: 40
    Units: kg/m3
    Limits: (None, None)
    Type: constant

    Specification of Resource Recovered from the Wastewater Treatment Plant
    """
    return 40


@cache('step')
def wtm_daily_maintenance():
    """
    Real Name: WTM Daily Maintenance
    Original Eqn: WTM Annual Maintenance / 365.25
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return wtm_annual_maintenance() / 365.25


@cache('step')
def mbr_daily_energy_consumption():
    """
    Real Name: MBR Daily Energy Consumption
    Original Eqn: MBR kWh per m3
    Units: KWh/Day
    Limits: (None, None)
    Type: component


    """
    return mbr_kwh_per_m3()


@cache('run')
def wwtw_unit_ferric_chloride():
    """
    Real Name: WWTW Unit Ferric Chloride
    Original Eqn: 0.0299
    Units: kg/m3
    Limits: (None, None)
    Type: constant

    Figure 5.23
    """
    return 0.0299


@cache('step')
def landuse_total_nitrogen():
    """
    Real Name: Landuse Total Nitrogen
    Original Eqn: Landuse1 Nitrogen+Landuse2 Nitrogen+Landuse3 Nitrogen+Landuse4 Nitrogen
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return landuse1_nitrogen() + landuse2_nitrogen() + landuse3_nitrogen() + landuse4_nitrogen()


@cache('step')
def swtw_daily_maintenance():
    """
    Real Name: SWTW Daily Maintenance
    Original Eqn: (SWTW Annual Maintenance/Days in a Year)*1e+006
    Units: $/Day
    Limits: (None, None)
    Type: component

    Maintenance and Replacement Costs on Daily Basis
    """
    return (swtw_annual_maintenance() / days_in_a_year()) * 1e+006


@cache('run')
def green_roof_space_requirements():
    """
    Real Name: Green Roof Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def treated_water():
    """
    Real Name: Treated Water
    Original Eqn: Distributed Treated Water
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return distributed_treated_water()


@cache('run')
def wp_flexibility_and_adaptability():
    """
    Real Name: WP Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def ia_roads_and_sidewalks_footprint():
    """
    Real Name: IA Roads and Sidewalks Footprint
    Original Eqn: 5000
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 5000


@cache('run')
def swtw_number_of_staff():
    """
    Real Name: SWTW Number of Staff
    Original Eqn: 2
    Units: Persons
    Limits: (None, None)
    Type: constant


    """
    return 2


@cache('step')
def retail_demand_variation_coefficient():
    """
    Real Name: Retail Demand Variation Coefficient
    Original Eqn: RANDOM UNIFORM( Retail Lower VC , Retail Upper VC , 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.random_uniform(retail_lower_vc(), retail_upper_vc(), 1)


integ_mbr_total_ghg_emission = functions.Integ(lambda: mbr_daily_ghg_emission(), lambda: 0)


@cache('run')
def wdm_construction():
    """
    Real Name: WDM Construction
    Original Eqn: 100
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 100


integ_swp_total_lcc = functions.Integ(lambda: swp_daily_costs(),
                                      lambda: swp_construction_and_installation())

integ_wwcs_lc_embodied_energy = functions.Integ(
    lambda: wwcs_emenergy_maintenance(),
    lambda: wwcs_construction_energy_m1() + wwcs_construction_energy_m2())


@cache('run')
def water_conduit_available_capacity():
    """
    Real Name: Water Conduit Available Capacity
    Original Eqn: 0.95
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.95


@cache('step')
def wtw_daily_maintenance():
    """
    Real Name: WTW Daily Maintenance
    Original Eqn: (WTW Annual Maintenance/Days in a Year)*1e+006
    Units: $/Day
    Limits: (None, None)
    Type: component

    Assumption: Maintenance and Replacements costs are 10% of Construction \n    \t\tCosts Per Year, this is why we divide it by 365 to get amount on a daily \n    \t\tscale
    """
    return (wtw_annual_maintenance() / days_in_a_year()) * 1e+006


@cache('run')
def restaurant_seats():
    """
    Real Name: Restaurant Seats
    Original Eqn: 1500
    Units: Seats
    Limits: (None, None)
    Type: constant

    Number of Seats in Restaurants\t\tSource: Water Resources Engineering, Larry W Mays, 2001 (Table 11.1.4. \n    \t\tPage 346)
    """
    return 1500


@cache('step')
def water_scarcity_counter():
    """
    Real Name: Water Scarcity Counter
    Original Eqn: IF THEN ELSE( Daily Water Demand >= System Water Capacity , 1 , 0 )
    Units: Binary
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(daily_water_demand() >= system_water_capacity(), 1, 0)


@cache('step')
def wtw_total_microsand_emenergy():
    """
    Real Name: WTW Total Microsand EmEnergy
    Original Eqn: WTW Total Microsand*WTW Unit Microsand EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wtw_total_microsand() * wtw_unit_microsand_emenergy()


@cache('run')
def wtw_water_resource_fee():
    """
    Real Name: WTW Water Resource Fee
    Original Eqn: 0.16
    Units: $
    Limits: (None, None)
    Type: constant

    $/m3
    """
    return 0.16


@cache('step')
def wdm_running_costs():
    """
    Real Name: WDM Running Costs
    Original Eqn: WDM Daily Maintenance Costs
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return wdm_daily_maintenance_costs()


integ_swt_ferric_chloride = functions.Integ(lambda: sw_daily_rate() * swtw_unit_ferric_chloride(),
                                            lambda: 0)


@cache('run')
def wwtw_unit_ferric_sulphate_emenergy():
    """
    Real Name: WWTW Unit Ferric Sulphate EmEnergy
    Original Eqn: 2
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 2


@cache('step')
def swtw_staff_costs():
    """
    Real Name: SWTW Staff Costs
    Original Eqn: (SWTW Average Salary*SWTW Number of Staff)/Days in a Year
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return (swtw_average_salary() * swtw_number_of_staff()) / days_in_a_year()


@cache('run')
def mf_faucet_demand():
    """
    Real Name: MF Faucet Demand
    Original Eqn: 29
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 29


@cache('run')
def wdm_unit_maintenance_ghg_m2():
    """
    Real Name: WDM Unit Maintenance GHG M2
    Original Eqn: 0.5
    Units: kgCO2eq/m
    Limits: (None, None)
    Type: constant


    """
    return 0.5


@cache('run')
def dem_hospitals_restroom():
    """
    Real Name: Dem Hospitals Restroom
    Original Eqn: 0.45
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.45


@cache('step')
def sf_stock_of_no_measure_units():
    """
    Real Name: SF Stock of No Measure Units
    Original Eqn: (1-SF Rate of Adoption)*SF Stock of Units
    Units: SF Units
    Limits: (None, None)
    Type: component


    """
    return (1 - sf_rate_of_adoption()) * sf_stock_of_units()


@cache('run')
def swcs_unit_construction_ghg_m2():
    """
    Real Name: SWCS Unit Construction GHG M2
    Original Eqn: 2.36
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 2.36


@cache('run')
def swcs_unit_construction_ghg_m1():
    """
    Real Name: SWCS Unit Construction GHG M1
    Original Eqn: 2.36
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant

    GHG Emissions per kg of Pipe Materials, Appendix A
    """
    return 2.36


@cache('run')
def ln_number_of_lm():
    """
    Real Name: LN Number of LM
    Original Eqn: 5
    Units: Number
    Limits: (None, None)
    Type: constant


    """
    return 5


@cache('run')
def green_roof_acceptability():
    """
    Real Name: Green Roof Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def wp_affordability():
    """
    Real Name: WP Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0, 1.0)
    Type: constant


    """
    return 1


@cache('run')
def wwp_affordability():
    """
    Real Name: WWP Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('step')
def rh_tank_outflow():
    """
    Real Name: RH Tank Outflow
    Original Eqn: IF THEN ELSE( RH Tank Current Storage Volume > 0 , RH Tank Current Storage Volume , \\ 0 )
    Units: m3
    Limits: (None, None)
    Type: component

    Ovde dodati Toilet, Irrigation, Deo za Industriju, i slicno!\t\t5 je random vrednost!
    """
    return functions.if_then_else(rh_tank_current_storage_volume() > 0,
                                  rh_tank_current_storage_volume(), 0)


@cache('step')
def swcs_lc_energy_embodied():
    """
    Real Name: SWCS LC Energy Embodied
    Original Eqn: INTEG ( SWCS EmEnergy Maintenance, SWCS Construction Energy M1 + SWCS Construction Energy M2)
    Units: KWh
    Limits: (None, None)
    Type: component

    Total Energy(kwh) required for SWS construction and maintenance\t\tInitial Value = Construction
    """
    return integ_swcs_lc_energy_embodied()


@cache('step')
def wwtw_total_methanol():
    """
    Real Name: WWTW Total Methanol
    Original Eqn: INTEG ( Treated Wastewater*WWTW Unit Methanol, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wwtw_total_methanol()


@cache('run')
def bioretention_affordability():
    """
    Real Name: Bioretention Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('step')
def wwcs_maintenance_ghg():
    """
    Real Name: WWCS Maintenance GHG
    Original Eqn: ((WWCS Unit Maintenance GHG M1*WWCS Number of Maintenance Trips)+(WWCS Unit Maintenance GHG M2\\ *WWCS Total Length M2))*WWCS Total Length M1
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return ((wwcs_unit_maintenance_ghg_m1() * wwcs_number_of_maintenance_trips()) +
            (wwcs_unit_maintenance_ghg_m2() * wwcs_total_length_m2())) * wwcs_total_length_m1()


@cache('step')
def wastewater_system_capacity():
    """
    Real Name: Wastewater System Capacity
    Original Eqn: WWTW Available Capacity*WWTW Daily Treatment Capacity
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return wwtw_available_capacity() * wwtw_daily_treatment_capacity()


@cache('step')
def wtw_total_carbon_dioxide_emenergy():
    """
    Real Name: WTW Total Carbon Dioxide EmEnergy
    Original Eqn: WTW Total Carbon Dioxide*WTW Unit Carbon Dioxide EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wtw_total_carbon_dioxide() * wtw_unit_carbon_dioxide_emenergy()


integ_wp_total_energy = functions.Integ(lambda: wp_daily_energy(), lambda: 0)


@cache('step')
def wwcs_daily_maintenance():
    """
    Real Name: WWCS Daily Maintenance
    Original Eqn: WWCS Annual Maintenance / 365.25
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return wwcs_annual_maintenance() / 365.25


@cache('step')
def wtw_total_alum():
    """
    Real Name: WTW Total Alum
    Original Eqn: INTEG ( Treated Water*WTW Unit Alum, 0)
    Units: kg
    Limits: (None, None)
    Type: component

    Total Amount of Alum required for Water Tretment
    """
    return integ_wtw_total_alum()


@cache('run')
def wdm_unit_maintenance_ghg_m1():
    """
    Real Name: WDM Unit Maintenance GHG M1
    Original Eqn: 0.5
    Units: kgCO2eq/m
    Limits: (None, None)
    Type: constant

    Energy Report, Table 2.3
    """
    return 0.5


@cache('run')
def cc_unit_demand():
    """
    Real Name: CC Unit Demand
    Original Eqn: 30
    Units: L/(m2*Day)
    Limits: (None, None)
    Type: constant


    """
    return 30


@cache('run')
def gws_reliability():
    """
    Real Name: GWS Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def wtw_unit_alum_emenergy():
    """
    Real Name: WTW Unit Alum EmEnergy
    Original Eqn: 0.89
    Units: KWh/kg
    Limits: (None, None)
    Type: constant

    Embodied energy kWh/kg for Alum (0.89)
    """
    return 0.89


@cache('run')
def wdm_annual_maintenance():
    """
    Real Name: WDM Annual Maintenance
    Original Eqn: 1.05
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 1.05


@cache('run')
def mf_wec_shower():
    """
    Real Name: MF WEC Shower
    Original Eqn: 1
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Water Efficiency Coefficient - Random
    """
    return 1


@cache('step')
def swt_ferric_chloride():
    """
    Real Name: SWT Ferric Chloride
    Original Eqn: INTEG ( SW Daily Rate*SWTW Unit Ferric Chloride, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_swt_ferric_chloride()


integ_rr_biogas_generated = functions.Integ(lambda: rr_daily_biogas(), lambda: 0)


@cache('run')
def bioswale_design_and_capital_costs():
    """
    Real Name: Bioswale Design and Capital Costs
    Original Eqn: 1000
    Units: $/m2
    Limits: (None, None)
    Type: constant


    """
    return 1000


@cache('run')
def sf_bathtub_demand():
    """
    Real Name: SF Bathtub Demand
    Original Eqn: 25
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 25


@cache('run')
def daycares_upper_vc():
    """
    Real Name: Daycares Upper VC
    Original Eqn: 0.85
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.85


integ_swp_total_ghg_emission = functions.Integ(lambda: swp_daily_ghg_emissions(), lambda: 0)


@cache('step')
def water_reuse_daily():
    """
    Real Name: Water Reuse Daily
    Original Eqn: GWS Tank Outflow + LM Inflow Total+ RH Tank Outflow
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return gws_tank_outflow() + lm_inflow_total() + rh_tank_outflow()


@cache('run')
def landuse2():
    """
    Real Name: Landuse2
    Original Eqn: 20000
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 20000


@cache('step')
def wwtw_total_calcium_hydroxide_emenergy():
    """
    Real Name: WWTW Total Calcium Hydroxide EmEnergy
    Original Eqn: WWTW Total Calcium Hydroxide*WWTW Unit Calcium Hydroxide EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_calcium_hydroxide() * wwtw_unit_calcium_hydroxide_emenergy()


@cache('run')
def wtw_unit_carbon_dioxide_ghg():
    """
    Real Name: WTW Unit Carbon Dioxide GHG
    Original Eqn: 0.794
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.794


@cache('step')
def green_roof_runoff_total():
    """
    Real Name: Green Roof Runoff Total
    Original Eqn: INTEG ( Green Roof Runoff Daily, 0)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return integ_green_roof_runoff_total()


@cache('run')
def gws_average_size_of_tank():
    """
    Real Name: GWS Average Size of Tank
    Original Eqn: 300
    Units: m3
    Limits: (None, None)
    Type: constant


    """
    return 300


@cache('run')
def wwtw_sludge_transport_and_disposal():
    """
    Real Name: WWTW Sludge Transport and Disposal
    Original Eqn: 1
    Units: $/kg
    Limits: (None, None)
    Type: constant

    Costs of Sludge Transport and Disposal Per 1kg
    """
    return 1


@cache('run')
def wwtw_unit_ethanol_ghg():
    """
    Real Name: WWTW Unit Ethanol GHG
    Original Eqn: 1.23
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 1.23


@cache('run')
def rhp_duration_of_pump_operation():
    """
    Real Name: RHP Duration of Pump Operation
    Original Eqn: 5
    Units: Hours
    Limits: (None, None)
    Type: constant

    Number of Hours for Pump Operations (Assumption is 24 hours)
    """
    return 5


integ_lm_total_lcc = functions.Integ(
    lambda: lm_daily_maintenance(), lambda: lm_installation_and_construction() * ln_number_of_lm())


@cache('run')
def sf_clothes_washer_demand():
    """
    Real Name: SF Clothes Washer Demand
    Original Eqn: 22
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 22


integ_biretention_lcc = functions.Integ(
    lambda: bioretention_daily_costs(),
    lambda: bioretention_design_and_capital_costs() * bioretention_footprint())


@cache('step')
def wp_daily_ghg_emissions():
    """
    Real Name: WP Daily GHG Emissions
    Original Eqn: WP Daily Energy*WP CO2 per kWh
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wp_daily_energy() * wp_co2_per_kwh()


@cache('step')
def result_system_ghg_emissions():
    """
    Real Name: Result System GHG Emissions
    Original Eqn: Result LID Embodied GHG + Result Network Embodied GHG Emissions + Result Pumping GHG Emissions\\ + Result RR GHG Emissions + Result Treatment GHG Emissions + Asphalt Construction GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return result_lid_embodied_ghg() + result_network_embodied_ghg_emissions(
    ) + result_pumping_ghg_emissions() + result_rr_ghg_emissions(
    ) + result_treatment_ghg_emissions() + asphalt_construction_ghg()


@cache('step')
def wwtw_daily_maintenance():
    """
    Real Name: WWTW Daily Maintenance
    Original Eqn: (WWTW Annual Maintenance/Days in a Year)*1e+006
    Units: $/Day
    Limits: (None, None)
    Type: component

    Maintenance and Replacement Costs on a Daily Level
    """
    return (wwtw_annual_maintenance() / days_in_a_year()) * 1e+006


@cache('run')
def wwtw_average_salary():
    """
    Real Name: WWTW Average Salary
    Original Eqn: 35000
    Units: $
    Limits: (None, None)
    Type: constant

    Average gross annual salary in Dollars
    """
    return 35000


@cache('step')
def dem_office_buildings():
    """
    Real Name: Dem Office Buildings
    Original Eqn: OB Unit Demand per m2*Footprint Office Buildings*OB Demand Variation Coefficient
    Units: L/Day
    Limits: (None, None)
    Type: component

    Water Distribution System Design PPT
    """
    return ob_unit_demand_per_m2() * footprint_office_buildings(
    ) * ob_demand_variation_coefficient()


@cache('step')
def wtw_embodied_energy_for_chemicals():
    """
    Real Name: WTW Embodied Energy for Chemicals
    Original Eqn: INTEG ( WTW Total Alum EmEnergy+WTW Total Calcium Hydroxide EmEnergy+WTW Total Carbon Dioxide EmEnergy\\ +WTW Total Microsand EmEnergy+WTW Total Polyaluminium Chloride EmEnergy+WTW Total Sodium Hypochlorite EmEnergy\\ , 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_embodied_energy_for_chemicals()


@cache('run')
def wp_price_per_kwh():
    """
    Real Name: WP Price per kWh
    Original Eqn: 0.11
    Units: $/KWh
    Limits: (0.0, 1.0)
    Type: constant

    Price of Energy (Dollars/Kwh)
    """
    return 0.11


@cache('run')
def swtw_construction_and_installation():
    """
    Real Name: SWTW Construction and Installation
    Original Eqn: 1.2
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 1.2


@cache('step')
def wwtw_total_ferric_sulphate():
    """
    Real Name: WWTW Total Ferric Sulphate
    Original Eqn: INTEG ( Treated Wastewater*WWTW Unit Ferric Sulphate, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wwtw_total_ferric_sulphate()


@cache('step')
def swcs_total_weight_m2():
    """
    Real Name: SWCS Total Weight M2
    Original Eqn: SWCS Total Length M2*SWCS Unit Weight M2
    Units: kg
    Limits: (None, None)
    Type: component

    Weight in Killograms for Material 2
    """
    return swcs_total_length_m2() * swcs_unit_weight_m2()


@cache('run')
def wwp_space_requirements():
    """
    Real Name: WWP Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def wtw_risk_to_human_health():
    """
    Real Name: WTW Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def dem_schools_restrooms():
    """
    Real Name: Dem Schools Restrooms
    Original Eqn: 0.33
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.33


@cache('run')
def bioretention_annual_maintenance_costs():
    """
    Real Name: Bioretention Annual Maintenance Costs
    Original Eqn: 5000
    Units: $/m2
    Limits: (None, None)
    Type: constant


    """
    return 5000


@cache('step')
def system_water_capacity():
    """
    Real Name: System Water Capacity
    Original Eqn: IF THEN ELSE( Water Conduit Reserved Capacity >= WTW Reserved Treatment Capacity , WTW Reserved Treatment Capacity\\ , Water Conduit Reserved Capacity )
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        water_conduit_reserved_capacity() >= wtw_reserved_treatment_capacity(),
        wtw_reserved_treatment_capacity(), water_conduit_reserved_capacity())


@cache('run')
def number_of_beds():
    """
    Real Name: Number of Beds
    Original Eqn: 280
    Units: Bed
    Limits: (None, None)
    Type: constant


    """
    return 280


@cache('run')
def wp_total_dynamic_head_of_pump():
    """
    Real Name: WP Total Dynamic Head of Pump
    Original Eqn: 10
    Units: m
    Limits: (None, None)
    Type: constant

    Total Dynamic Head of Pump(m)
    """
    return 10


@cache('run')
def wwcs_unit_weight_m2():
    """
    Real Name: WWCS Unit Weight M2
    Original Eqn: 10
    Units: kg/m
    Limits: (None, None)
    Type: constant

    Material 2
    """
    return 10


@cache('run')
def wwcs_unit_weight_m1():
    """
    Real Name: WWCS Unit Weight M1
    Original Eqn: 10
    Units: kg/m
    Limits: (None, None)
    Type: constant

    Unit Weight of 1m' of Material (PVC, PE, Mild Steel, Concrete, etc)
    """
    return 10


@cache('step')
def rr_total_urea_generated():
    """
    Real Name: RR Total Urea Generated
    Original Eqn: INTEG ( RR Daily Urea, 0)
    Units: 
    Limits: (None, None)
    Type: component


    """
    return integ_rr_total_urea_generated()


@cache('step')
def gws_total_volume():
    """
    Real Name: GWS Total Volume
    Original Eqn: GWS Average Size of Tank * GWS Number of Tanks
    Units: m3
    Limits: (None, None)
    Type: component

    Volume of Greywater Tanks in Cubic Meters(m3) on the neighbrhood scale
    """
    return gws_average_size_of_tank() * gws_number_of_tanks()


@cache('run')
def wwtw_unit_ferric_sulphate():
    """
    Real Name: WWTW Unit Ferric Sulphate
    Original Eqn: 0.0215
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.0215


@cache('step')
def landuse3_daily_nitrogen():
    """
    Real Name: Landuse3 Daily Nitrogen
    Original Eqn: Landuse3 EMC Nitrogen*Landuse3 Percentage*Qv
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return landuse3_emc_nitrogen() * landuse3_percentage() * qv()


@cache('run')
def number_of_students():
    """
    Real Name: Number of Students
    Original Eqn: 2500
    Units: Persons
    Limits: (None, None)
    Type: constant


    """
    return 2500


@cache('step')
def swcs_construction_ghg_m2():
    """
    Real Name: SWCS Construction GHG M2
    Original Eqn: SWCS Total Weight M2*SWCS Unit Construction GHG M2
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return swcs_total_weight_m2() * swcs_unit_construction_ghg_m2()


@cache('run')
def wtw_unit_microsand_emenergy():
    """
    Real Name: WTW Unit Microsand EmEnergy
    Original Eqn: 0.06
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.06


@cache('step')
def swtw_running_costs():
    """
    Real Name: SWTW Running Costs
    Original Eqn: SWTW Staff Costs+(SWTW Electricity for treatment*SW Daily Rate*Electricity Fee)+SWTW Daily Maintenance
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return swtw_staff_costs() + (swtw_electricity_for_treatment() * sw_daily_rate() *
                                 electricity_fee()) + swtw_daily_maintenance()


@cache('step')
def dem_hvac():
    """
    Real Name: Dem HVAC
    Original Eqn: Full Load Water Use * HVAC Hours of Operation * HVAC Demand Variation Coefficient
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return full_load_water_use() * hvac_hours_of_operation() * hvac_demand_variation_coefficient()


@cache('step')
def wtw_total_carbon_dioxide_ghg():
    """
    Real Name: WTW Total Carbon Dioxide GHG
    Original Eqn: WTW Total Carbon Dioxide*WTW Unit Carbon Dioxide GHG
    Units: 
    Limits: (None, None)
    Type: component


    """
    return wtw_total_carbon_dioxide() * wtw_unit_carbon_dioxide_ghg()


@cache('run')
def water_supply_leakage_rate():
    """
    Real Name: Water Supply Leakage Rate
    Original Eqn: 0.05
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.05


@cache('step')
def wtw_total_polyaluminium_chloride():
    """
    Real Name: WTW Total Polyaluminium Chloride
    Original Eqn: INTEG ( Treated Water*WTW Unit Polyaluminium Chloride, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_total_polyaluminium_chloride()


integ_wtw_operation_ghg = functions.Integ(
    lambda: ghg_emission_generation_electricity_factor() * wtw_operation_energy(), lambda: 0)


@cache('step')
def rr_total_ammonium_nitrate_generated():
    """
    Real Name: RR Total Ammonium Nitrate Generated
    Original Eqn: INTEG ( RR Daily Ammonium Nitrate, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_rr_total_ammonium_nitrate_generated()


@cache('step')
def biretention_lcc():
    """
    Real Name: Biretention LCC
    Original Eqn: INTEG ( Bioretention Daily Costs, Bioretention Design and Capital Costs * Bioretention Footprint)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_biretention_lcc()


@cache('run')
def swp_acceptability():
    """
    Real Name: SWP Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


integ_wtw_total_alum = functions.Integ(lambda: treated_water() * wtw_unit_alum(), lambda: 0)


@cache('run')
def rb_design_and_capital_costs():
    """
    Real Name: RB Design and Capital Costs
    Original Eqn: 700
    Units: $/m3
    Limits: (None, None)
    Type: constant

    CVC Manual\t\tThe capital cost to homeowners of an individual rainwater harvesting \n    \t\tsystem can range between $6,000 and $14,000 (in 2006 Canadian dollars), \n    \t\tdepending on its size and configuration (CMHC, 2009). Based on analysis by \n    \t\tthe Center for Watershed Protection (2007b), base construction costs per \n    \t\tcubic metre of runoff stored (in 2006 US dollars) range from $212 to $777, \n    \t\twith a median of $530 (CWP, 2007b).
    """
    return 700


@cache('run')
def wwp_acceptability():
    """
    Real Name: WWP Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def lm_ghg_per_m3():
    """
    Real Name: LM GHG per m3
    Original Eqn: 18
    Units: kgCO2eq/m3
    Limits: (None, None)
    Type: constant

    Figure 3. LCA results for the decentralized LM treatment and water reuse \n    \t\tsystem. (a) Annualized results for the analysis period (25 years) for the \n    \t\tentire system per ML of influent that is treated and recycled.
    """
    return 18


@cache('step')
def wdm_maintenance_ghg():
    """
    Real Name: WDM Maintenance GHG
    Original Eqn: ((WDM Unit Maintenance GHG M1*WDM Number of Maintenance Trips)+(WDM Unit Maintenance GHG M2\\ *WDM Total Length M2))*WDM Total Length M1
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return ((wdm_unit_maintenance_ghg_m1() * wdm_number_of_maintenance_trips()) +
            (wdm_unit_maintenance_ghg_m2() * wdm_total_length_m2())) * wdm_total_length_m1()


@cache('run')
def rhp_unit_conversion_factor():
    """
    Real Name: RHP Unit Conversion Factor
    Original Eqn: 101.9
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 101.9


integ_wdm_lc_embodied_energy = functions.Integ(
    lambda: wdm_emenergy_maintenance(),
    lambda: wdm_construction_energy_m1() + wdm_construction_energy_m2())


@cache('run')
def lm_acceptability():
    """
    Real Name: LM Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('step')
def wwcs_total_costs():
    """
    Real Name: WWCS Total Costs
    Original Eqn: INTEG ( WWCS Running Costs, WWCS Construction + WWCS Replacement + WWCS Disposal)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_wwcs_total_costs()


@cache('step')
def wwp_daily_maintenance():
    """
    Real Name: WWP Daily Maintenance
    Original Eqn: WWP Annual Maintenance/Days in a Year
    Units: $
    Limits: (None, None)
    Type: component


    """
    return wwp_annual_maintenance() / days_in_a_year()


@cache('run')
def gws_annual_maintenance_costs():
    """
    Real Name: GWS Annual Maintenance Costs
    Original Eqn: 5000
    Units: $
    Limits: (None, None)
    Type: constant

    Using Graywater and Stormwater to Enhance Local Water Supplies: An Assessment of \n    \t\tRisks, Costs, and Benefits\t\tTable 7.1 Cost of Graywater Treatment and Storage Systems of Varying Scale, \n    \t\tIncluding a Coarse Filter and Chlorine Disinfection\t\tSystem
    """
    return 5000


@cache('step')
def sw_daily_rate():
    """
    Real Name: SW Daily Rate
    Original Eqn: Qv*0.001
    Units: m3
    Limits: (None, None)
    Type: component

    0.001 - 1mm = 1 L -> Qv(mm)*0.001 = m3
    """
    return qv() * 0.001


integ_rhp_total_lcc = functions.Integ(
    lambda: rhp_daily_costs(),
    lambda: (rhp_construction_and_installation()) * rhp_number_of_pumps())


@cache('run')
def wwp_motor_efficiency():
    """
    Real Name: WWP Motor Efficiency
    Original Eqn: 80
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Motor Efficiency [%]
    """
    return 80


@cache('run')
def wwp_co2_per_kwh():
    """
    Real Name: WWP CO2 per kWh
    Original Eqn: 0.05
    Units: kgCO2/KWh
    Limits: (None, None)
    Type: constant

    kgCO2 per kWh for Ontario, Canada
    """
    return 0.05


@cache('run')
def wtm_replacement():
    """
    Real Name: WTM Replacement
    Original Eqn: 8
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 8


@cache('run')
def rhp_average_dynamic_head():
    """
    Real Name: RHP Average Dynamic Head
    Original Eqn: 100
    Units: m
    Limits: (None, None)
    Type: constant

    Total Dynamic Head of Pump(m)
    """
    return 100


@cache('step')
def rhp_total_energy():
    """
    Real Name: RHP Total Energy
    Original Eqn: INTEG ( RHP Daily Energy, 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_rhp_total_energy()


@cache('run')
def cc_lower_vc():
    """
    Real Name: CC Lower VC
    Original Eqn: 1.22
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1.22


@cache('step')
def asphalt_construction_ghg():
    """
    Real Name: Asphalt Construction GHG
    Original Eqn: Asphalt Unit GHG Emissions * ( IA Parking Footprint + IA Roads and Sidewalks Footprint\\ )
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return asphalt_unit_ghg_emissions() * (
        ia_parking_footprint() + ia_roads_and_sidewalks_footprint())


@cache('step')
def swp_daily_costs():
    """
    Real Name: SWP Daily Costs
    Original Eqn: SWP Daily Maintenance + ((SWP Unit Conversion Factor * SWP Total Dynamic Head of Pump\\ * SWP Duration of Pump Operation * WP Price per kWh * (SW Daily Rate * 0.0115741)) / (SWP Motor Efficiency * SWP Pump Efficiency * SWP Variable Speed Drive Efficiency\\ ))
    Units: $/Day
    Limits: (None, None)
    Type: component

    Calculating Energy Costs, Chapter 10.8, page 439 Advanced Water Distribution Modeling\t\t0.0115741 is m3/day into l/s
    """
    return swp_daily_maintenance() + (
        (swp_unit_conversion_factor() * swp_total_dynamic_head_of_pump() *
         swp_duration_of_pump_operation() * wp_price_per_kwh() * (sw_daily_rate() * 0.0115741)) /
        (swp_motor_efficiency() * swp_pump_efficiency() * swp_variable_speed_drive_efficiency()))


@cache('step')
def bioretention_daily_costs():
    """
    Real Name: Bioretention Daily Costs
    Original Eqn: Bioretention Annual Maintenance Costs * Bioretention Footprint
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return bioretention_annual_maintenance_costs() * bioretention_footprint()


@cache('run')
def sf_decommissioned_units_annually():
    """
    Real Name: SF Decommissioned Units Annually
    Original Eqn: 200
    Units: SF Units
    Limits: (None, None)
    Type: constant

    Number of single-family units removed from the neighborhood annually
    """
    return 200


@cache('step')
def swcs_total_weight_m1():
    """
    Real Name: SWCS Total Weight M1
    Original Eqn: SWS Total Length M1*SWCS Unit Weight M1
    Units: kg
    Limits: (None, None)
    Type: component

    Total Weight of Stormwater System (in Killograms)
    """
    return sws_total_length_m1() * swcs_unit_weight_m1()


@cache('run')
def wwtw_unit_nitric_acid_ghg():
    """
    Real Name: WWTW Unit Nitric Acid GHG
    Original Eqn: 6.3
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 6.3


@cache('run')
def gwp_number_of_pumps():
    """
    Real Name: GWP Number of Pumps
    Original Eqn: 3
    Units: Number
    Limits: (None, None)
    Type: constant

    Number of Pumps in Greywater System
    """
    return 3


@cache('run')
def mf_wec_faucet():
    """
    Real Name: MF WEC Faucet
    Original Eqn: 1
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Water Efficiency Coefficient - Random
    """
    return 1


@cache('run')
def rhp_pump_efficiency():
    """
    Real Name: RHP Pump Efficiency
    Original Eqn: 93
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Pump Efficiency [%]
    """
    return 93


@cache('run')
def swp_variable_speed_drive_efficiency():
    """
    Real Name: SWP Variable Speed Drive Efficiency
    Original Eqn: 88
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Variable Speed Drive Efficiency [%]
    """
    return 88


@cache('step')
def sf_stock_of_water_sensitive_units():
    """
    Real Name: SF Stock of Water Sensitive Units
    Original Eqn: SF Rate of Adoption*SF Stock of Units
    Units: SF Units
    Limits: (None, None)
    Type: component


    """
    return sf_rate_of_adoption() * sf_stock_of_units()


@cache('run')
def wwp_total_dynamic_head():
    """
    Real Name: WWP Total Dynamic Head
    Original Eqn: 50
    Units: m
    Limits: (None, None)
    Type: constant

    Total Dynamic Head of Pump(m)
    """
    return 50


@cache('run')
def wwtw_annual_maintenance():
    """
    Real Name: WWTW Annual Maintenance
    Original Eqn: 1.5
    Units: Percentage
    Limits: (None, None)
    Type: constant

    WWTW Maintenance and Replacement Costs on Annual Basis (in Millions of $)
    """
    return 1.5


@cache('step')
def wwtw_total_nitric_acid_emenergy():
    """
    Real Name: WWTW Total Nitric Acid EmEnergy
    Original Eqn: WWTW Total Nitric Acid*WWTW Unit Nitric Acid EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_nitric_acid() * wwtw_unit_nitric_acid_emenergy()


@cache('step')
def swp_total_lcc():
    """
    Real Name: SWP Total LCC
    Original Eqn: INTEG ( SWP Daily Costs, SWP Construction and Installation)
    Units: $
    Limits: (None, None)
    Type: component

    Costs of Pumping Station Installation
    """
    return integ_swp_total_lcc()


@cache('run')
def electricity_fee():
    """
    Real Name: Electricity Fee
    Original Eqn: 0.11
    Units: $/KWh
    Limits: (None, None)
    Type: constant

    Price of electricity in Dollars per kWh
    """
    return 0.11


@cache('step')
def wwtw_total_ethanol():
    """
    Real Name: WWTW Total Ethanol
    Original Eqn: INTEG ( Treated Wastewater*WWTW Unit Ethanol, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wwtw_total_ethanol()


@cache('run')
def mf_rate_of_adoption():
    """
    Real Name: MF Rate of Adoption
    Original Eqn: 0.55
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.55


@cache('run')
def sf_dishwasher_demand():
    """
    Real Name: SF Dishwasher Demand
    Original Eqn: 4
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 4


@cache('run')
def gwp_unit_conversion_factor():
    """
    Real Name: GWP Unit Conversion Factor
    Original Eqn: 101.9
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 101.9


@cache('run')
def ia_runoff_coefficient():
    """
    Real Name: IA Runoff Coefficient
    Original Eqn: 0.85
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.85


@cache('step')
def wtm_total_costs():
    """
    Real Name: WTM Total Costs
    Original Eqn: INTEG ( WTM Running Costs, WTM Construction + WTM Disposal + WTM Replacement)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_wtm_total_costs()


@cache('run')
def bioretention_risk_to_human_health():
    """
    Real Name: Bioretention Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def wwtw_unit_ferric_chloride_ghg():
    """
    Real Name: WWTW Unit Ferric Chloride GHG
    Original Eqn: 0.26
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.26


integ_rr_total_ammonium_nitrate_generated = functions.Integ(lambda: rr_daily_ammonium_nitrate(),
                                                            lambda: 0)


@cache('run')
def sf_leaks():
    """
    Real Name: SF Leaks
    Original Eqn: 20
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 20


@cache('run')
def pp_design_and_capital_costs():
    """
    Real Name: PP Design and Capital Costs
    Original Eqn: 1200
    Units: $/m2
    Limits: (None, None)
    Type: constant


    """
    return 1200


@cache('step')
def lm_daily_maintenance():
    """
    Real Name: LM Daily Maintenance
    Original Eqn: LM Annual Maintenance / Days in a Year
    Units: $/Day
    Limits: (None, None)
    Type: component

    Daily Costs of LM Maintenance
    """
    return lm_annual_maintenance() / days_in_a_year()


@cache('run')
def sf_wec_clothes_washer():
    """
    Real Name: SF WEC Clothes Washer
    Original Eqn: 0.88
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.88


@cache('run')
def swp_risk_to_human_health():
    """
    Real Name: SWP Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def public_spaces_for_irrigation():
    """
    Real Name: Public spaces for Irrigation
    Original Eqn: 25000
    Units: m2
    Limits: (None, None)
    Type: constant

    Total Irrigated Area on the Neighborhood Level
    """
    return 25000


@cache('run')
def wp_motor_efficiency():
    """
    Real Name: WP Motor Efficiency
    Original Eqn: 80
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Motor Efficiency [%]
    """
    return 80


@cache('run')
def mbr_reliability():
    """
    Real Name: MBR Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 4


@cache('step')
def rhp_total_ghg_emission():
    """
    Real Name: RHP Total GHG Emission
    Original Eqn: INTEG ( RHP Daily GHG Emissions, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_rhp_total_ghg_emission()


@cache('step')
def wtw_embodied_ghg_for_chemicals():
    """
    Real Name: WTW Embodied GHG for Chemicals
    Original Eqn: INTEG ( WTW Total Polyaluminium Chloride GHG+WTW Total Alum GHG+WTW Total Calcium Hydroxide GHG\\ +WTW Total Carbon Dioxide GHG+WTW Total Microsand GHG+WTW Total Sodium Hypochlorite GHG\\ , 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_embodied_ghg_for_chemicals()


@cache('step')
def sf_units_decomissioned():
    """
    Real Name: SF Units Decomissioned
    Original Eqn: SF Decommissioned Units Annually/Days in a Year
    Units: SF Units/Day
    Limits: (None, None)
    Type: component


    """
    return sf_decommissioned_units_annually() / days_in_a_year()


@cache('step')
def wwtw_total_ferric_sulphate_emenergy():
    """
    Real Name: WWTW Total Ferric Sulphate EmEnergy
    Original Eqn: WWTW Total Ferric Sulphate*WWTW Unit Ferric Sulphate EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_ferric_sulphate() * wwtw_unit_ferric_sulphate_emenergy()


@cache('run')
def pp_footprint():
    """
    Real Name: PP Footprint
    Original Eqn: 150000
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 150000


@cache('run')
def porous_pavement_acceptability():
    """
    Real Name: Porous Pavement Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def wwtw_unit_methanol():
    """
    Real Name: WWTW Unit Methanol
    Original Eqn: 0.0329
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.0329


@cache('run')
def swp_flexibility_and_adaptability():
    """
    Real Name: SWP Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def gwp_construction_and_installation():
    """
    Real Name: GWP Construction and Installation
    Original Eqn: 150000
    Units: $
    Limits: (None, None)
    Type: constant

    Installation Costs in $
    """
    return 150000


@cache('run')
def industrial_floor_area():
    """
    Real Name: Industrial Floor Area
    Original Eqn: 10000
    Units: m2
    Limits: (None, None)
    Type: constant

    m2 of Industrial Area (10000 is an assumption)
    """
    return 10000


@cache('step')
def result_system_energy():
    """
    Real Name: Result System Energy
    Original Eqn: Result Network Embodied Energy + Result Pumping Energy + Result RR Energy + Result Treatment Embodied Energy\\ + Asphalt Construction Energy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return result_network_embodied_energy() + result_pumping_energy() + result_rr_energy(
    ) + result_treatment_embodied_energy() + asphalt_construction_energy()


@cache('run')
def wwtw_affordability():
    """
    Real Name: WWTW Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('run')
def mbr_capacity():
    """
    Real Name: MBR Capacity
    Original Eqn: 150
    Units: m3/Day
    Limits: (None, None)
    Type: constant

    Prices for 151 m3/day, 302 m3/day, 3785 m3/day
    """
    return 150


@cache('step')
def gwp_total_energy():
    """
    Real Name: GWP Total Energy
    Original Eqn: INTEG ( GWP Daily Energy, 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_gwp_total_energy()


integ_wp_total_ghg_emission = functions.Integ(lambda: wp_daily_ghg_emissions(), lambda: 0)


@cache('run')
def sf_average_occupancy_per_unit():
    """
    Real Name: SF Average Occupancy per Unit
    Original Eqn: 3
    Units: Persons
    Limits: (None, None)
    Type: constant

    Average number of persons living in a single family household unit
    """
    return 3


@cache('step')
def wtw_total_calcium_hydroxide_emenergy():
    """
    Real Name: WTW Total Calcium Hydroxide EmEnergy
    Original Eqn: WTW Total Calcium Hydroxide*WTW Unit Calcium Hydroxide EmEnergy
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return wtw_total_calcium_hydroxide() * wtw_unit_calcium_hydroxide_emenergy()


integ_wtw_total_microsand = functions.Integ(lambda: treated_water() * wtw_unit_microsand(),
                                            lambda: 0)


@cache('run')
def mf_new_units_annually():
    """
    Real Name: MF New Units Annually
    Original Eqn: 1500
    Units: MF Units
    Limits: (None, None)
    Type: constant


    """
    return 1500


@cache('step')
def gws_tank_outflow():
    """
    Real Name: GWS Tank Outflow
    Original Eqn: IF THEN ELSE( GWP Current Storage Volume > 0 , GWP Current Storage Volume , 0 )
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(gwp_current_storage_volume() > 0, gwp_current_storage_volume(),
                                  0)


@cache('step')
def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: Day
    Limits: (0.0, None)
    Type: component

    The frequency with which output is stored.
    """
    return time_step()


@cache('step')
def wtw_total_sodium_hypochlorite_ghg():
    """
    Real Name: WTW Total Sodium Hypochlorite GHG
    Original Eqn: INTEG ( WTW Total Sodium Hypochlorite * WTW Unit Sodium Hypochlorite GHG, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_total_sodium_hypochlorite_ghg()


integ_wtw_total_calcium_hydroxide = functions.Integ(
    lambda: treated_water() * wtw_unit_calcium_hydroxide(), lambda: 0)


integ_gws_total_lcc = functions.Integ(lambda: gws_daily_maintenance(), lambda: (gws_plumbing_costs_per_m2()*gws_plumbing_area())+gws_total_installation_and_construction_costs())


@cache('step')
def wwcs_construction_ghg_m2():
    """
    Real Name: WWCS Construction GHG M2
    Original Eqn: WWCS Total Weight M2*WWCS Unit Construction GHG M2
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wwcs_total_weight_m2() * wwcs_unit_construction_ghg_m2()


@cache('step')
def wwcs_construction_ghg_m1():
    """
    Real Name: WWCS Construction GHG M1
    Original Eqn: WWCS Total Weight M1*WWCS Unit Construction GHG M1
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wwcs_total_weight_m1() * wwcs_unit_construction_ghg_m1()


@cache('run')
def green_roof_construction_ghg():
    """
    Real Name: Green Roof Construction GHG
    Original Eqn: 28.1
    Units: kgCO2eq/m2
    Limits: (None, None)
    Type: constant

    Table 2.3 Energy Consumption and CO2 Emissions Indicators for Drainage System \n    \t\tConstruction and Maintenance\t\tReport on Energy in the Urban Water Cycle Table 2.3
    """
    return 28.1


@cache('step')
def mf_stock_of_units():
    """
    Real Name: MF Stock of Units
    Original Eqn: INTEG ( MF New Units-MF Units Decomissioned, MF Initial Stock of Units)
    Units: MF Units
    Limits: (None, None)
    Type: component

    6000 Multi-family Households Initial Value
    """
    return integ_mf_stock_of_units()


integ_wtw_total_costs = functions.Integ(
    lambda: wtw_running_costs(),
    lambda: (wtw_construction_and_installation() + wtw_capital_investment()) * 1e+006)


@cache('step')
def result_rr_energy():
    """
    Real Name: Result RR Energy
    Original Eqn: RHP Total Energy + GWP Total Energy + LM Total Energy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return rhp_total_energy() + gwp_total_energy() + lm_total_energy()


@cache('step')
def wwp_daily_costs():
    """
    Real Name: WWP Daily Costs
    Original Eqn: (WWP Unit Conversion Factor * WWP Total Dynamic Head * WWP Duration of Pump Operation\\ * WWP Price per kWh * (Wastewater Treated * 0.0115741)) / (WWP Motor Efficiency*WWP Pump Efficiency*WWP Variable Speed Drive Efficiency\\ ) + WWP Daily Maintenance
    Units: $/Day
    Limits: (None, None)
    Type: component

    * 0.0115741 Conversion factor m3/day in liters/second
    """
    return (wwp_unit_conversion_factor() * wwp_total_dynamic_head() *
            wwp_duration_of_pump_operation() * wwp_price_per_kwh() *
            (wastewater_treated() * 0.0115741)) / (wwp_motor_efficiency() * wwp_pump_efficiency(
            ) * wwp_variable_speed_drive_efficiency()) + wwp_daily_maintenance()


@cache('step')
def pp_percentage():
    """
    Real Name: PP Percentage
    Original Eqn: (100*PP Footprint)/LU Sum
    Units: Percentage
    Limits: (None, None)
    Type: component


    """
    return (100 * pp_footprint()) / lu_sum()


@cache('run')
def unit_demand_per_student():
    """
    Real Name: Unit Demand Per Student
    Original Eqn: 25.1
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant


    """
    return 25.1


@cache('step')
def result_treatment_ghg_emissions():
    """
    Real Name: Result Treatment GHG Emissions
    Original Eqn: WTW Embodied GHG for Chemicals + WWTW Embodied GHG for Chemicals + WTW Operation GHG\\ + WWTW Operation GHG + SWT Total Ferric Chloride GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wtw_embodied_ghg_for_chemicals() + wwtw_embodied_ghg_for_chemicals(
    ) + wtw_operation_ghg() + wwtw_operation_ghg() + swt_total_ferric_chloride_ghg()


@cache('step')
def wwtw_embodied_energy_for_chemicals():
    """
    Real Name: WWTW Embodied Energy for Chemicals
    Original Eqn: INTEG ( WWTW Total Calcium Hydroxide EmEnergy+WWTW Total Ethanol EmEnergy+WWTW Total Ferric Chloride EmEnergy\\ +WWTW Total Ferric Sulphate EmEnergy+WWTW Total Methanol EmEnergy+WWTW Total Nitric Acid EmEnergy\\ , 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_wwtw_embodied_energy_for_chemicals()


@cache('step')
def gwp_total_lcc():
    """
    Real Name: GWP Total LCC
    Original Eqn: INTEG ( GWP Daily Costs, (GWP Construction and Installation)*GWP Number of Pumps)
    Units: $
    Limits: (None, None)
    Type: component

    Costs of Pumping Station Installation
    """
    return integ_gwp_total_lcc()


@cache('run')
def wwcs_unit_maintenance_ghg_m1():
    """
    Real Name: WWCS Unit Maintenance GHG M1
    Original Eqn: 0.5
    Units: kgCO2eq/m
    Limits: (None, None)
    Type: constant

    Energy Report, Table 2.3
    """
    return 0.5


@cache('run')
def wwcs_unit_maintenance_ghg_m2():
    """
    Real Name: WWCS Unit Maintenance GHG M2
    Original Eqn: 0.5
    Units: kgCO2eq/m
    Limits: (None, None)
    Type: constant


    """
    return 0.5


@cache('run')
def asphalt_unit_energy():
    """
    Real Name: Asphalt Unit Energy
    Original Eqn: 1.1
    Units: KWh/m2
    Limits: (None, None)
    Type: constant

    Assumption
    """
    return 1.1


@cache('step')
def irrigation_demand():
    """
    Real Name: Irrigation Demand
    Original Eqn: Unit Irrigation Demand * (SF Total Area for Irrigation+Public spaces for Irrigation)\\ * Coefficient of Seasonal Variation in Irrigation Demand * 0.001
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return unit_irrigation_demand() * (
        sf_total_area_for_irrigation() + public_spaces_for_irrigation()
    ) * coefficient_of_seasonal_variation_in_irrigation_demand() * 0.001


@cache('run')
def rhp_number_of_pumps():
    """
    Real Name: RHP Number of Pumps
    Original Eqn: 1
    Units: Number
    Limits: (None, None)
    Type: constant

    Number of Pumps in Greywater System
    """
    return 1


@cache('step')
def swcs_maintenance_ghg():
    """
    Real Name: SWCS Maintenance GHG
    Original Eqn: ((SWCS Unit Maintenance GHG M1*SWCS Number of Maintenance Trips)+(SWCS Unit Maintenance GHG M2\\ *SWCS Total Length M2))*SWS Total Length M1
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return ((swcs_unit_maintenance_ghg_m1() * swcs_number_of_maintenance_trips()) +
            (swcs_unit_maintenance_ghg_m2() * swcs_total_length_m2())) * sws_total_length_m1()


@cache('run')
def green_roof_cn_value():
    """
    Real Name: Green Roof CN Value
    Original Eqn: 78
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 78


@cache('run')
def rwh_flexibility_and_adaptability():
    """
    Real Name: RWH Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def gwp_daily_maintenance():
    """
    Real Name: GWP Daily Maintenance
    Original Eqn: GWP Annual Maintenance/Days in a Year
    Units: $
    Limits: (None, None)
    Type: component


    """
    return gwp_annual_maintenance() / days_in_a_year()


@cache('step')
def daycares_demand_variation_coefficient():
    """
    Real Name: Daycares Demand Variation Coefficient
    Original Eqn: RANDOM UNIFORM( Daycares Lower VC , Daycares Upper VC , 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.random_uniform(daycares_lower_vc(), daycares_upper_vc(), 1)


@cache('run')
def retail_lower_vc():
    """
    Real Name: Retail Lower VC
    Original Eqn: 0.91
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.91


@cache('run')
def days_in_a_year():
    """
    Real Name: Days in a Year
    Original Eqn: 365.25
    Units: Day
    Limits: (365.0, 366.0, 0.2)
    Type: constant

    Number of Years (Calculation Purposes)
    """
    return 365.25


integ_landuse2_nitrogen = functions.Integ(lambda: landuse2_daily_nitrogen(), lambda: 0)


@cache('step')
def wtw_total_sodium_hypochlorite_emenergy():
    """
    Real Name: WTW Total Sodium Hypochlorite EmEnergy
    Original Eqn: WTW Total Sodium Hypochlorite*WTW Unit Sodium Hypochlorite EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wtw_total_sodium_hypochlorite() * wtw_unit_sodium_hypochlorite_emenergy()


@cache('run')
def gwp_motor_efficiency():
    """
    Real Name: GWP Motor Efficiency
    Original Eqn: 80
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Motor Efficiency [%]
    """
    return 80


@cache('run')
def wwp_construction_and_installation():
    """
    Real Name: WWP Construction and Installation
    Original Eqn: 1.5e+006
    Units: $
    Limits: (None, None)
    Type: constant

    Installation and Construction Costs for Wastewater Pumping Station in $
    """
    return 1.5e+006


@cache('run')
def hvac_hours_of_operation():
    """
    Real Name: HVAC Hours of Operation
    Original Eqn: 18
    Units: Hours
    Limits: (None, None)
    Type: constant


    """
    return 18


@cache('run')
def mf_initial_stock_of_units():
    """
    Real Name: MF Initial Stock of Units
    Original Eqn: 6000
    Units: MF Units
    Limits: (None, None)
    Type: constant


    """
    return 6000


@cache('run')
def gws_plumbing_area():
    """
    Real Name: GWS Plumbing Area
    Original Eqn: 3000
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3000


@cache('run')
def unit_demand_per_child():
    """
    Real Name: Unit Demand per Child
    Original Eqn: 25
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant


    """
    return 25


@cache('step')
def gwp_daily_ghg_emissions():
    """
    Real Name: GWP Daily GHG Emissions
    Original Eqn: GWP Daily Energy*WP CO2 per kWh
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return gwp_daily_energy() * wp_co2_per_kwh()


@cache('run')
def swtw_annual_maintenance():
    """
    Real Name: SWTW Annual Maintenance
    Original Eqn: 1.2
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Maintenance and Replacement Costs on Annual Basis (in Millions of $)
    """
    return 1.2


@cache('run')
def rhp_variable_speed_drive_efficiency():
    """
    Real Name: RHP Variable Speed Drive Efficiency
    Original Eqn: 88
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Variable Speed Drive Efficiency [%]
    """
    return 88


@cache('step')
def rhp_daily_energy():
    """
    Real Name: RHP Daily Energy
    Original Eqn: ((RH Tank Outflow*0.0115741*RHP Duration of Pump Operation*RHP Average Dynamic Head*\\ RHP Unit Conversion Factor)/(RHP Motor Efficiency *RHP Pump Efficiency*RHP Variable Speed Drive Efficiency))*RHP Number of Pumps
    Units: KWh/Day
    Limits: (None, None)
    Type: component

    Daily Energy Consumption required for Drinking Water Pumping\t\t*0.0115741 Conversion factor m3/day into l/s
    """
    return (
        (rh_tank_outflow() * 0.0115741 * rhp_duration_of_pump_operation() *
         rhp_average_dynamic_head() * rhp_unit_conversion_factor()) /
        (rhp_motor_efficiency() * rhp_pump_efficiency() * rhp_variable_speed_drive_efficiency())
    ) * rhp_number_of_pumps()


@cache('run')
def wwtw_unit_ferric_chloride_emenergy():
    """
    Real Name: WWTW Unit Ferric Chloride EmEnergy
    Original Eqn: 1.39
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 1.39


@cache('run')
def unit_demand_of_retail_space():
    """
    Real Name: Unit Demand of Retail Space
    Original Eqn: 4.3
    Units: L/(Day*m2)
    Limits: (None, None)
    Type: constant


    """
    return 4.3


@cache('step')
def dem_hotels():
    """
    Real Name: Dem Hotels
    Original Eqn: Unit Demand per m2*Footprint Hotels
    Units: L/Day
    Limits: (None, None)
    Type: component

    Source: Water Resources Engineering, Larry W Mays, 2001 (Table 11.1.4. Page 346)\t\tWater Distribution System Design PPT
    """
    return unit_demand_per_m2() * footprint_hotels()


integ_mbr_total_energy = functions.Integ(lambda: -mbr_daily_energy_consumption(), lambda: 0)


@cache('run')
def rhp_construction_and_installation():
    """
    Real Name: RHP Construction and Installation
    Original Eqn: 150000
    Units: $
    Limits: (None, None)
    Type: constant

    Installation Costs in $
    """
    return 150000


@cache('run')
def mbr_flexibility_and_adaptability():
    """
    Real Name: MBR Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def swtw_electricity_for_treatment():
    """
    Real Name: SWTW Electricity for treatment
    Original Eqn: 0.5
    Units: KWh/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.5


@cache('step')
def water_conduit_reserved_capacity():
    """
    Real Name: Water Conduit Reserved Capacity
    Original Eqn: Water Conduit Available Capacity*Water Conduit Daily Capacity
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return water_conduit_available_capacity() * water_conduit_daily_capacity()


@cache('step')
def qv():
    """
    Real Name: Qv
    Original Eqn: Qh*LU Sum
    Units: mm
    Limits: (None, None)
    Type: component


    """
    return qh() * lu_sum()


@cache('step')
def wp_daily_energy():
    """
    Real Name: WP Daily Energy
    Original Eqn: (Distributed Treated Water* 0.0115741 * WP Duration of Pump Operation * WP Total Dynamic Head of Pump\\ * WP Unit Conversion Factor )/(WP Motor Efficiency * WP Pump Efficiency * WP Variable Speed Drive Efficiency)
    Units: KWh/Day
    Limits: (None, None)
    Type: component

    Daily Energy Consumption required for Drinking Water Pumping\t\t* 0.0115741 Conversion factor m3/day in liters/second
    """
    return (
        distributed_treated_water() * 0.0115741 * wp_duration_of_pump_operation() *
        wp_total_dynamic_head_of_pump() * wp_unit_conversion_factor()) / (
            wp_motor_efficiency() * wp_pump_efficiency() * wp_variable_speed_drive_efficiency())


@cache('step')
def rh_control():
    """
    Real Name: RH Control
    Original Eqn: IF THEN ELSE( RH Tank Current Storage Volume >= RB and Cistern Storage Volume, 0 , 1\\ )
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Proveriti Logiku IF STATEMENT-a
    """
    return functions.if_then_else(
        rh_tank_current_storage_volume() >= rb_and_cistern_storage_volume(), 0, 1)


@cache('step')
def swp_daily_maintenance():
    """
    Real Name: SWP Daily Maintenance
    Original Eqn: SWP Annual Maintenance/Days in a Year
    Units: $
    Limits: (None, None)
    Type: component


    """
    return swp_annual_maintenance() / days_in_a_year()


@cache('step')
def swp_total_energy():
    """
    Real Name: SWP Total Energy
    Original Eqn: INTEG ( SWP Daily Energy, 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_swp_total_energy()


@cache('run')
def lm_installation_and_construction():
    """
    Real Name: LM Installation and Construction
    Original Eqn: 1.4e+006
    Units: $
    Limits: (None, None)
    Type: constant

    For 151 m3/day\t302 m3/day\t3785 m3/day
    """
    return 1.4e+006


@cache('run')
def lm_kwh_per_m3():
    """
    Real Name: LM kWh per m3
    Original Eqn: 4.5
    Units: KWh/m3
    Limits: (None, None)
    Type: constant

    Figure 3. LCA results for the decentralized LM treatment and water reuse \n    \t\tsystem. (a) Annualized results for the analysis period (25 years) for the \n    \t\tentire system per ML of influent that is treated and recycled. - System \n    \t\tMaterials, Settling Tank Emissions, Pumping, Treatment
    """
    return 4.5


@cache('step')
def wwtw_total_ferric_chloride_emenergy():
    """
    Real Name: WWTW Total Ferric Chloride EmEnergy
    Original Eqn: WWTW Total Ferric Chloride*WWTW Unit Ferric Chloride EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_ferric_chloride() * wwtw_unit_ferric_chloride_emenergy()


@cache('run')
def pp_cn_value():
    """
    Real Name: PP CN Value
    Original Eqn: 67
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Proveriti Vrednost u LTHIA-LID Manual
    """
    return 67


@cache('step')
def lm_total_energy():
    """
    Real Name: LM Total Energy
    Original Eqn: INTEG ( LM Daily Energy Consumption, 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_lm_total_energy()


@cache('step')
def result_rr_ghg_emissions():
    """
    Real Name: Result RR GHG Emissions
    Original Eqn: RHP Total GHG Emission + GWP Total GHG Emission + LM Total GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return rhp_total_ghg_emission() + gwp_total_ghg_emission() + lm_total_ghg()


@cache('run')
def rb_and_cistern_annual_maintenance_costs():
    """
    Real Name: RB and Cistern Annual Maintenance Costs
    Original Eqn: 150
    Units: $/m3
    Limits: (None, None)
    Type: constant

    Rainwater Harvesting Tool Assumption
    """
    return 150


@cache('run')
def wtw_unit_sodium_hypochlorite():
    """
    Real Name: WTW Unit Sodium Hypochlorite
    Original Eqn: 0.00293
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.00293


@cache('step')
def gwp_total_ghg_emission():
    """
    Real Name: GWP Total GHG Emission
    Original Eqn: INTEG ( GWP Daily GHG Emissions, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_gwp_total_ghg_emission()


@cache('step')
def swt_total_ferric_chloride_emenergy():
    """
    Real Name: SWT Total Ferric Chloride EmEnergy
    Original Eqn: SWT Ferric Chloride*SWTW Unit Ferric Chloride EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return swt_ferric_chloride() * swtw_unit_ferric_chloride_emenergy()


@cache('step')
def mf_stock_of_no_measure_units():
    """
    Real Name: MF Stock of No Measure Units
    Original Eqn: (1-MF Rate of Adoption)*MF Stock of Units
    Units: MF Units
    Limits: (None, None)
    Type: component


    """
    return (1 - mf_rate_of_adoption()) * mf_stock_of_units()


@cache('run')
def sw_release_rate():
    """
    Real Name: SW Release Rate
    Original Eqn: 50
    Units: m3/Day
    Limits: (None, None)
    Type: constant


    """
    return 50


@cache('run')
def swtw_acceptability():
    """
    Real Name: SWTW Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('step')
def rr_daily_ammonium_nitrate():
    """
    Real Name: RR Daily Ammonium Nitrate
    Original Eqn: RR Unit Ammonium Nitrate*Wastewater Treated
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return rr_unit_ammonium_nitrate() * wastewater_treated()


@cache('run')
def wtw_acceptability():
    """
    Real Name: WTW Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (1.0, 5.0, 1.0)
    Type: constant


    """
    return 3


@cache('run')
def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 0
    Units: Day
    Limits: (None, None)
    Type: constant

    The initial time for the simulation.
    """
    return 0


@cache('run')
def porous_pavement_flexibility_and_adaptability():
    """
    Real Name: Porous Pavement Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def wwtw_total_ferric_chloride_ghg():
    """
    Real Name: WWTW Total Ferric Chloride GHG
    Original Eqn: WWTW Total Ferric Chloride*WWTW Unit Ferric Chloride GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_ferric_chloride() * wwtw_unit_ferric_chloride_ghg()


@cache('step')
def days_with_higher_demand():
    """
    Real Name: Days With Higher Demand
    Original Eqn: Water Scarcity Counter
    Units: m3/Day
    Limits: (None, None)
    Type: component

    Difference Between Water Demand and Raw Water Intake Capacity
    """
    return water_scarcity_counter()


@cache('run')
def wp_unit_conversion_factor():
    """
    Real Name: WP Unit Conversion Factor
    Original Eqn: 101.9
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 101.9


@cache('step')
def sf_stock_of_units():
    """
    Real Name: SF Stock of Units
    Original Eqn: INTEG ( INTEGER( SF New Units-SF Units Decomissioned ), SF Initial Stock of Units)
    Units: SF Units
    Limits: (None, None)
    Type: component


    """
    return integ_sf_stock_of_units()


@cache('step')
def swcs_lc_embodied_ghg():
    """
    Real Name: SWCS LC Embodied GHG
    Original Eqn: INTEG ( SWCS Maintenance GHG, SWCS Construction GHG M1+SWCS Construction GHG M2)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_swcs_lc_embodied_ghg()


@cache('run')
def wtw_average_staff_salary():
    """
    Real Name: WTW Average Staff Salary
    Original Eqn: 40000
    Units: $
    Limits: (None, None)
    Type: constant

    35.000 Annual Gross Salary / 365 to get the daily value
    """
    return 40000


@cache('run')
def wwtw_unit_calcium_hydroxide_ghg():
    """
    Real Name: WWTW Unit Calcium Hydroxide GHG
    Original Eqn: 0.763
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.763


@cache('step')
def wwcs_construction_energy_m1():
    """
    Real Name: WWCS Construction Energy M1
    Original Eqn: WWCS Total Weight M1*WWCS Unit Construction Energy M1
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wwcs_total_weight_m1() * wwcs_unit_construction_energy_m1()


integ_wwtw_total_methanol = functions.Integ(lambda: treated_wastewater() * wwtw_unit_methanol(),
                                            lambda: 0)

integ_bioswale_lcc = functions.Integ(
    lambda: bioswale_daily_costs(),
    lambda: bioswale_design_and_capital_costs() * bioswale_footprint())

integ_lm_total_ghg = functions.Integ(lambda: lm_daily_ghg_emission(), lambda: 0)


@cache('run')
def wwtw_number_of_staff():
    """
    Real Name: WWTW Number of Staff
    Original Eqn: 15
    Units: Persons
    Limits: (None, None)
    Type: constant

    Number of Person required for operation of the wastewater treatment plant
    """
    return 15


@cache('run')
def rr_unit_emenergy_urea():
    """
    Real Name: RR Unit EmEnergy Urea
    Original Eqn: 4.81
    Units: KWh/kg
    Limits: (None, None)
    Type: constant

    Table 5.26
    """
    return 4.81


@cache('run')
def lm_risk_to_human_health():
    """
    Real Name: LM Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def footprint_hotels():
    """
    Real Name: Footprint Hotels
    Original Eqn: 80000
    Units: m2
    Limits: (None, None)
    Type: constant

    Source: Water Resources Engineering, Larry W Mays, 2001 (Table 11.1.4. \n    \t\tPage 346)
    """
    return 80000


@cache('step')
def wtw_total_carbon_dioxide():
    """
    Real Name: WTW Total Carbon Dioxide
    Original Eqn: INTEG ( Treated Water * WTW Unit Carbon Dioxide, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_total_carbon_dioxide()


@cache('run')
def sf_wec_shower():
    """
    Real Name: SF WEC Shower
    Original Eqn: 0.7
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.7


@cache('step')
def rhp_daily_costs():
    """
    Real Name: RHP Daily Costs
    Original Eqn: ((RHP Unit Conversion Factor * RHP Average Dynamic Head * RHP Duration of Pump Operation\\ * WP Price per kWh * (RH Tank Outflow * 0.0115741)) / (RHP Motor Efficiency*RHP Pump Efficiency*RHP Variable Speed Drive Efficiency\\ ) + RHP Daily Maintenance)*RHP Number of Pumps
    Units: $/Day
    Limits: (None, None)
    Type: component

    Calculating Energy Costs, Chapter 10.8, page 439 Advanced Water Distribution Modeling\t\t* 0.0115741 Conversion Factor m3/day l/s
    """
    return (
        (rhp_unit_conversion_factor() * rhp_average_dynamic_head() *
         rhp_duration_of_pump_operation() * wp_price_per_kwh() * (rh_tank_outflow() * 0.0115741)) /
        (rhp_motor_efficiency() * rhp_pump_efficiency() * rhp_variable_speed_drive_efficiency()) +
        rhp_daily_maintenance()) * rhp_number_of_pumps()


@cache('step')
def result_treatment_embodied_energy():
    """
    Real Name: Result Treatment Embodied Energy
    Original Eqn: WTW Embodied Energy for Chemicals + WWTW Embodied Energy for Chemicals + WTW Operation Energy\\ + WWTW Operation Electricity + SWT Total Ferric Chloride EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component

    Total embodied and operational energy required for water, wastewater and \n    \t\tstormwater treatment
    """
    return wtw_embodied_energy_for_chemicals() + wwtw_embodied_energy_for_chemicals(
    ) + wtw_operation_energy() + wwtw_operation_electricity() + swt_total_ferric_chloride_emenergy(
    )


@cache('run')
def ia_parking_footprint():
    """
    Real Name: IA Parking Footprint
    Original Eqn: 12000
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 12000


integ_rhp_total_energy = functions.Integ(lambda: rhp_daily_energy(), lambda: 0)


@cache('run')
def swcs_annual_maintenance():
    """
    Real Name: SWCS Annual Maintenance
    Original Eqn: 1.05
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 1.05


@cache('step')
def swcs_daily_maintenance():
    """
    Real Name: SWCS Daily Maintenance
    Original Eqn: SWCS Annual Maintenance / 365.25
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return swcs_annual_maintenance() / 365.25


@cache('step')
def wdm_number_of_maintenance_trips():
    """
    Real Name: WDM Number of Maintenance Trips
    Original Eqn: 2/Days in a Year
    Units: Number
    Limits: (None, None)
    Type: component

    Number of Trips Per Year
    """
    return 2 / days_in_a_year()


@cache('run')
def green_roof_affordability():
    """
    Real Name: Green Roof Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('run')
def sf_other():
    """
    Real Name: SF Other
    Original Eqn: 25
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    Other - refers to other water demand, such as swimming pools...\t\tAccording to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 25


@cache('run')
def sf_wec_bathtub():
    """
    Real Name: SF WEC Bathtub
    Original Eqn: 0.66
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.66


@cache('step')
def industrial_demand():
    """
    Real Name: Industrial Demand
    Original Eqn: Industrial Floor Area * Unit Industrial Demand Per Floor Area * Industrial Demand Variation Coefficient\\ * 0.001
    Units: m3/Day
    Limits: (None, None)
    Type: component

    Keating Channel Precinct Plan, Section 13 - 13.2.2.3 Design Considerations
    """
    return industrial_floor_area() * unit_industrial_demand_per_floor_area(
    ) * industrial_demand_variation_coefficient() * 0.001


@cache('step')
def result_system_reliability():
    """
    Real Name: Result System Reliability
    Original Eqn: Bioretention Reliability+Bioswale Reliability+Green Roof Reliability+GWS Reliability\\ +LM Reliability+MBR Reliability+Porous Pavement Reliability+RWH Reliability+SWP Reliability\\ +SWTW Reliability+WP Reliability+WTW Reliability+WWP Reliability+WWTW Reliability
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return bioretention_reliability() + bioswale_reliability() + green_roof_reliability(
    ) + gws_reliability() + lm_reliability() + mbr_reliability() + porous_pavement_reliability(
    ) + rwh_reliability() + swp_reliability() + swtw_reliability() + wp_reliability(
    ) + wtw_reliability() + wwp_reliability() + wwtw_reliability()


@cache('step')
def s():
    """
    Real Name: S
    Original Eqn: (25400/CN Composite)-254
    Units: Dmnl
    Limits: (None, None)
    Type: component

    CN Composite Number for different land use and green infrastructure
    """
    return (25400 / cn_composite()) - 254


@cache('run')
def bioswale_cn_value():
    """
    Real Name: Bioswale CN Value
    Original Eqn: 42
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 42


@cache('run')
def rb_and_cistern_footprint():
    """
    Real Name: RB and Cistern Footprint
    Original Eqn: 0
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def wp_reliability():
    """
    Real Name: WP Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0, 1.0)
    Type: constant


    """
    return 4


@cache('step')
def stormwater_tank():
    """
    Real Name: Stormwater Tank
    Original Eqn: INTEG ( SW Daily Rate-SW Release Rate, 0)
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return integ_stormwater_tank()


integ_wtw_total_sodium_hypochlorite_ghg = functions.Integ(
    lambda: wtw_total_sodium_hypochlorite() * wtw_unit_sodium_hypochlorite_ghg(), lambda: 0)


@cache('run')
def gwp_average_dynamic_head():
    """
    Real Name: GWP Average Dynamic Head
    Original Eqn: 100
    Units: m
    Limits: (None, None)
    Type: constant

    Total Dynamic Head of Pump(m)
    """
    return 100


@cache('run')
def bioretention_construction_ghg():
    """
    Real Name: Bioretention Construction GHG
    Original Eqn: 0.2115
    Units: kgCO2eq/m2
    Limits: (None, None)
    Type: constant

    Table 2.3 Energy Consumption and CO2 Emissions Indicators for Drainage \n    \t\tSystem Construction and Maintenance
    """
    return 0.2115


@cache('step')
def result_lid_embodied_ghg():
    """
    Real Name: Result LID Embodied GHG
    Original Eqn: Bioretention Total Construction GHG + Bioswale Total Construction GHG + Green Roof Total Construction GHG\\ + PP Total Construction GHG + RH System Total Construction GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return bioretention_total_construction_ghg() + bioswale_total_construction_ghg(
    ) + green_roof_total_construction_ghg() + pp_total_construction_ghg(
    ) + rh_system_total_construction_ghg()


@cache('step')
def wtw_total_polyaluminium_chloride_emenergy():
    """
    Real Name: WTW Total Polyaluminium Chloride EmEnergy
    Original Eqn: WTW Total Polyaluminium Chloride*WTW Unit Polyaluminium Chloride EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wtw_total_polyaluminium_chloride() * wtw_unit_polyaluminium_chloride_emenergy()


integ_wtw_embodied_energy_for_chemicals = functions.Integ(lambda: wtw_total_alum_emenergy()+wtw_total_calcium_hydroxide_emenergy()+wtw_total_carbon_dioxide_emenergy()+wtw_total_microsand_emenergy()+wtw_total_polyaluminium_chloride_emenergy()+wtw_total_sodium_hypochlorite_emenergy(), lambda: 0)


@cache('step')
def wwp_daily_ghg_emissions():
    """
    Real Name: WWP Daily GHG Emissions
    Original Eqn: WWP Daily Energy*WWP CO2 per kWh
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wwp_daily_energy() * wwp_co2_per_kwh()


@cache('step')
def green_roof_daily_costs():
    """
    Real Name: Green Roof Daily Costs
    Original Eqn: (Green Roof Annual Maintenance Costs * Green Roof Footprint)/365.25
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return (green_roof_annual_maintenance_costs() * green_roof_footprint()) / 365.25


@cache('run')
def gws_space_requirements():
    """
    Real Name: GWS Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 365
    Units: Day
    Limits: (None, None)
    Type: constant

    The final time for the simulation.
    """
    return 365


@cache('run')
def mbr_space_requirements():
    """
    Real Name: MBR Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


integ_wtw_total_polyaluminium_chloride_ghg = functions.Integ(
    lambda: wtw_total_polyaluminium_chloride() * wtw_unit_polyaluimium_chloride_ghg(), lambda: 0)


@cache('run')
def wtw_unit_microsand_ghg():
    """
    Real Name: WTW Unit Microsand GHG
    Original Eqn: 0.021
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.021


integ_wwtw_total_ferric_chloride = functions.Integ(
    lambda: treated_wastewater() * wwtw_unit_ferric_chloride(), lambda: 0)


@cache('run')
def swcs_construction():
    """
    Real Name: SWCS Construction
    Original Eqn: 100
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 100


@cache('step')
def dem_hospitals():
    """
    Real Name: Dem Hospitals
    Original Eqn: Number of Beds * Unit Demand per Bed
    Units: L/Day
    Limits: (None, None)
    Type: component


    """
    return number_of_beds() * unit_demand_per_bed()


@cache('step')
def wwcs_emenergy_maintenance():
    """
    Real Name: WWCS EmEnergy Maintenance
    Original Eqn: ((WWCS Total Length M1*WWCS Unit Maintenance Energy M1)+(WWCS Unit Maintenance Energy M2\\ *WWCS Total Length M2))*WWCS Number of Maintenance Trips
    Units: KWh/Day
    Limits: (None, None)
    Type: component


    """
    return ((wwcs_total_length_m1() * wwcs_unit_maintenance_energy_m1()) +
            (wwcs_unit_maintenance_energy_m2() * wwcs_total_length_m2())
            ) * wwcs_number_of_maintenance_trips()


@cache('run')
def wwp_flexibility_and_adaptability():
    """
    Real Name: WWP Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


integ_wwtw_total_calcium_hydroxide = functions.Integ(
    lambda: treated_wastewater() * wwtw_unit_calcium_hydroxide(), lambda: 0)


@cache('step')
def landuse4_nitrogen():
    """
    Real Name: Landuse4 Nitrogen
    Original Eqn: INTEG ( Landuse4 Daily Nitrogen, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_landuse4_nitrogen()


@cache('run')
def wwtw_unit_nitric_acid():
    """
    Real Name: WWTW Unit Nitric Acid
    Original Eqn: 0.0245
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.0245


@cache('run')
def pp_construction_ghg():
    """
    Real Name: PP Construction GHG
    Original Eqn: 29.2
    Units: kgCO2eq/m2
    Limits: (None, None)
    Type: constant

    Report on Energy in the Urban Water Cycle Table 2.3
    """
    return 29.2


@cache('step')
def rr_daily_urea():
    """
    Real Name: RR Daily Urea
    Original Eqn: RR Unit Urea*Wastewater Treated
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return rr_unit_urea() * wastewater_treated()


integ_wwtw_operation_electricity = functions.Integ(
    lambda: wwtw_treated_wastewater() * wwtw_electricity_for_treatment_of_m3(), lambda: 0)


@cache('run')
def wwcs_construction():
    """
    Real Name: WWCS Construction
    Original Eqn: 100
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 100


@cache('run')
def gwp_variable_speed_drive_efficiency():
    """
    Real Name: GWP Variable Speed Drive Efficiency
    Original Eqn: 88
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Variable Speed Drive Efficiency [%]
    """
    return 88


integ_sf_stock_of_units = functions.Integ(lambda: int(sf_new_units() - sf_units_decomissioned()),
                                          lambda: sf_initial_stock_of_units())


@cache('run')
def wwcs_disposal():
    """
    Real Name: WWCS Disposal
    Original Eqn: 0
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def landuse2_daily_nitrogen():
    """
    Real Name: Landuse2 Daily Nitrogen
    Original Eqn: Landuse2 EMC Nitrogen*Landuse2 Percentage*Qv
    Units: mg/L
    Limits: (None, None)
    Type: component


    """
    return landuse2_emc_nitrogen() * landuse2_percentage() * qv()


@cache('run')
def landuse1_emc_nitrogen():
    """
    Real Name: Landuse1 EMC Nitrogen
    Original Eqn: 0.7
    Units: mg/L
    Limits: (0.4, 5.5, 0.1)
    Type: constant

    LTHIA-LID EMC Concetration Value Matrix for Commercila, Industrial, \n    \t\tResidential, Grass pasture, Agriculture, Forest
    """
    return 0.7


@cache('step')
def landuse4_percentage():
    """
    Real Name: Landuse4 Percentage
    Original Eqn: (100*Landuse4)/LU Sum
    Units: Percentage
    Limits: (None, None)
    Type: component


    """
    return (100 * landuse4()) / lu_sum()


@cache('step')
def wtw_operation_energy():
    """
    Real Name: WTW Operation Energy
    Original Eqn: INTEG ( WTW Operation Daily Energy, 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_operation_energy()


@cache('step')
def result_pumping_energy():
    """
    Real Name: Result Pumping Energy
    Original Eqn: SWP Total Energy+WP Total Energy+WWP Total Energy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return swp_total_energy() + wp_total_energy() + wwp_total_energy()


@cache('step')
def bioretention_total_construction_ghg():
    """
    Real Name: Bioretention Total Construction GHG
    Original Eqn: Bioretention Construction GHG * Bioretention Footprint
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return bioretention_construction_ghg() * bioretention_footprint()


@cache('run')
def swp_total_dynamic_head_of_pump():
    """
    Real Name: SWP Total Dynamic Head of Pump
    Original Eqn: 10
    Units: m
    Limits: (None, None)
    Type: constant

    Total Dynamic Head of Pump(m)
    """
    return 10


@cache('step')
def wwtw_administration_costs():
    """
    Real Name: WWTW Administration Costs
    Original Eqn: WWTW Administration Rate*WWTW Staff Costs
    Units: $
    Limits: (None, None)
    Type: component


    """
    return wwtw_administration_rate() * wwtw_staff_costs()


@cache('step')
def gws_daily_maintenance():
    """
    Real Name: GWS Daily Maintenance
    Original Eqn: GWS Annual Maintenance Costs / Days in a Year
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return gws_annual_maintenance_costs() / days_in_a_year()


@cache('step')
def result_system_flexibility_and_adaptability():
    """
    Real Name: Result System Flexibility and Adaptability
    Original Eqn: Bioretention Flexibility and Adaptability+Bioswale Flexibility and Adaptability+Green Roof Flexibility and Adaptability\\ +GWS Flexibility and Adaptability+LM Flexibility and Adaptability+MBR Flexibility and Adaptability\\ +Porous Pavement Flexibility and Adaptability+RWH Flexibility and Adaptability+SWP Flexibility and Adaptability\\ +SWTW Flexibility and Adaptability+WP Flexibility and Adaptability+WTW Flexibility and Adaptability\\ +WWP Flexibility and Adaptability+WWTW Flexibility and Adaptability
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return bioretention_flexibility_and_adaptability() + bioswale_flexibility_and_adaptability(
    ) + green_roof_flexibility_and_adaptability() + gws_flexibility_and_adaptability(
    ) + lm_flexibility_and_adaptability() + mbr_flexibility_and_adaptability(
    ) + porous_pavement_flexibility_and_adaptability() + rwh_flexibility_and_adaptability(
    ) + swp_flexibility_and_adaptability() + swtw_flexibility_and_adaptability(
    ) + wp_flexibility_and_adaptability() + wtw_flexibility_and_adaptability(
    ) + wwp_flexibility_and_adaptability() + wwtw_flexibility_and_adaptability()


@cache('run')
def wp_annual_maintenance():
    """
    Real Name: WP Annual Maintenance
    Original Eqn: 10000
    Units: $
    Limits: (None, None)
    Type: constant

    Percentage of Initial Costs
    """
    return 10000


@cache('run')
def wwcs_replacement():
    """
    Real Name: WWCS Replacement
    Original Eqn: 0
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def lm_inflow_office_buildings():
    """
    Real Name: LM Inflow Office Buildings
    Original Eqn: Dem Office Buildings*LM Percentage of OB*Dem OB Restroom
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return dem_office_buildings() * lm_percentage_of_ob() * dem_ob_restroom()


@cache('run')
def wwtw_unit_ethanol_emenergy():
    """
    Real Name: WWTW Unit Ethanol EmEnergy
    Original Eqn: 0.83
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.83


@cache('run')
def retail_space_in_m2():
    """
    Real Name: Retail space in m2
    Original Eqn: 20000
    Units: m2
    Limits: (None, None)
    Type: constant

    m2 of Sales area
    """
    return 20000


@cache('run')
def bioswale_space_requirements():
    """
    Real Name: Bioswale Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def wp_total_ghg_emission():
    """
    Real Name: WP Total GHG Emission
    Original Eqn: INTEG ( WP Daily GHG Emissions, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_wp_total_ghg_emission()


@cache('step')
def mbr_total_lcc():
    """
    Real Name: MBR Total LCC
    Original Eqn: INTEG ( MBR Daily Maintenance, MBR Installation and Construction Costs * MBR Number of MBR)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_mbr_total_lcc()


@cache('run')
def landuse3_emc_nitrogen():
    """
    Real Name: Landuse3 EMC Nitrogen
    Original Eqn: 4.4
    Units: mg/L
    Limits: (0.4, 5.5)
    Type: constant

    LTHIA-LID EMC Concetration Value Matrix for Commercila, Industrial, \n    \t\tResidential, Grass pasture, Agriculture, Forest
    """
    return 4.4


@cache('run')
def mbr_risk_to_human_health():
    """
    Real Name: MBR Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def unit_demand_per_m2():
    """
    Real Name: Unit Demand per m2
    Original Eqn: 10.5
    Units: L/Day/m2
    Limits: (None, None)
    Type: constant

    Source: Water Resources Engineering, Larry W Mays, 2001 (Table 11.1.4. \n    \t\tPage 346)
    """
    return 10.5


@cache('step')
def result_system_total_lcc():
    """
    Real Name: Result System Total LCC
    Original Eqn: Result LID LCC + Result Network LCC + Result Pumping LCC + Result RR LCC + Result Treatment LCC\\ + Asphalt Capital Costs
    Units: $
    Limits: (None, None)
    Type: component


    """
    return result_lid_lcc() + result_network_lcc() + result_pumping_lcc() + result_rr_lcc(
    ) + result_treatment_lcc() + asphalt_capital_costs()


@cache('step')
def sf_new_units():
    """
    Real Name: SF New Units
    Original Eqn: INTEGER( SF New Units Annually/Days in a Year )
    Units: SF Units/Day
    Limits: (None, None)
    Type: component


    """
    return int(sf_new_units_annually() / days_in_a_year())


integ_gwp_current_storage_volume = functions.Integ(lambda: gws_tank_inflow() - gws_tank_outflow(),
                                                   lambda: 0)


@cache('step')
def gwp_daily_energy():
    """
    Real Name: GWP Daily Energy
    Original Eqn: ((GWS Tank Outflow*0.0115741*GWP Duration of Pump Operation*GWP Average Dynamic Head\\ *GWP Unit Conversion Factor)/(GWP Motor Efficiency *GWP Pump Efficiency*GWP Variable Speed Drive Efficiency))*GWP Number of Pumps
    Units: KWh/Day
    Limits: (None, None)
    Type: component

    Daily Energy Consumption required for Drinking Water Pumping\t\t*0.0115741 Conversion factor m3/day into l/s
    """
    return (
        (gws_tank_outflow() * 0.0115741 * gwp_duration_of_pump_operation() *
         gwp_average_dynamic_head() * gwp_unit_conversion_factor()) /
        (gwp_motor_efficiency() * gwp_pump_efficiency() * gwp_variable_speed_drive_efficiency())
    ) * gwp_number_of_pumps()


@cache('run')
def mbr_number_of_mbr():
    """
    Real Name: MBR Number of MBR
    Original Eqn: 5
    Units: Number
    Limits: (None, None)
    Type: constant


    """
    return 5


@cache('step')
def wtw_total_microsand_ghg():
    """
    Real Name: WTW Total Microsand GHG
    Original Eqn: WTW Total Microsand*WTW Unit Microsand GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wtw_total_microsand() * wtw_unit_microsand_ghg()


@cache('run')
def lm_flexibility_and_adaptability():
    """
    Real Name: LM Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def lm_affordability():
    """
    Real Name: LM Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('run')
def wsc_replacement():
    """
    Real Name: WSC Replacement
    Original Eqn: 50
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 50


@cache('run')
def restaurants_lower_vc():
    """
    Real Name: Restaurants Lower VC
    Original Eqn: 0.78
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.78


@cache('run')
def swtw_average_salary():
    """
    Real Name: SWTW Average Salary
    Original Eqn: 50000
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 50000


@cache('run')
def swcs_total_length_m2():
    """
    Real Name: SWCS Total Length M2
    Original Eqn: 2500
    Units: m
    Limits: (None, None)
    Type: constant


    """
    return 2500


@cache('run')
def wsc_disposal():
    """
    Real Name: WSC Disposal
    Original Eqn: 10
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 10


@cache('run')
def wwtw_acceptability():
    """
    Real Name: WWTW Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def swcs_unit_maintenance_energy_m1():
    """
    Real Name: SWCS Unit Maintenance Energy M1
    Original Eqn: 0.05
    Units: KWh/m
    Limits: (None, None)
    Type: constant

    Energy Report, Table 2.3
    """
    return 0.05


integ_wdm_total_costs = functions.Integ(
    lambda: wdm_running_costs(), lambda: wdm_construction() + wdm_replacement() + wdm_disposal())


@cache('step')
def wwtw_total_costs():
    """
    Real Name: WWTW Total Costs
    Original Eqn: INTEG ( WWTW Running Costs, (WWTW Construction and Installation + WWTW Capital Investment)*1e+006)
    Units: $
    Limits: (None, None)
    Type: component

    Total Costs of Construction, Operation and Maintenance for WWTW
    """
    return integ_wwtw_total_costs()


@cache('run')
def wdm_total_length_m2():
    """
    Real Name: WDM Total Length M2
    Original Eqn: 2500
    Units: m
    Limits: (None, None)
    Type: constant


    """
    return 2500


@cache('run')
def wtw_administration_rate():
    """
    Real Name: WTW Administration Rate
    Original Eqn: 0.5
    Units: Percentage
    Limits: (None, None)
    Type: constant

    50% of Staff Costs, Daily
    """
    return 0.5


integ_swp_total_energy = functions.Integ(lambda: swp_daily_energy(), lambda: 0)


@cache('run')
def wtw_daily_treatment_capacity():
    """
    Real Name: WTW Daily Treatment Capacity
    Original Eqn: 950000
    Units: m3/Day
    Limits: (None, None)
    Type: constant

    RC Harris Rated Daily Treatment Capacity
    """
    return 950000


@cache('run')
def swp_duration_of_pump_operation():
    """
    Real Name: SWP Duration of Pump Operation
    Original Eqn: 24
    Units: Hours
    Limits: (None, None)
    Type: constant

    Number of Hours for Pump Operations (Assumption is 24 hours)
    """
    return 24


@cache('run')
def gwp_pump_efficiency():
    """
    Real Name: GWP Pump Efficiency
    Original Eqn: 93
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Pump Efficiency [%]
    """
    return 93


@cache('step')
def wp_daily_maintenance():
    """
    Real Name: WP Daily Maintenance
    Original Eqn: WP Annual Maintenance/Days in a Year
    Units: $
    Limits: (None, None)
    Type: component


    """
    return wp_annual_maintenance() / days_in_a_year()


@cache('run')
def asphalt_unit_ghg_emissions():
    """
    Real Name: Asphalt Unit GHG Emissions
    Original Eqn: 0.6
    Units: kgCO2eq/m2
    Limits: (None, None)
    Type: constant

    Assumption
    """
    return 0.6


@cache('run')
def gwp_duration_of_pump_operation():
    """
    Real Name: GWP Duration of Pump Operation
    Original Eqn: 5
    Units: Hours
    Limits: (None, None)
    Type: constant

    Number of Hours for Pump Operations (Assumption is 24 hours)
    """
    return 5


integ_wwtw_total_ferric_sulphate = functions.Integ(
    lambda: treated_wastewater() * wwtw_unit_ferric_sulphate(), lambda: 0)


@cache('step')
def neighborhood_population():
    """
    Real Name: Neighborhood Population
    Original Eqn: MF Average Occupancy per Unit*MF Stock of Units+SF Average Occupancy per Unit*SF Stock of Units
    Units: Persons
    Limits: (None, None)
    Type: component

    Neighborhood population in number of inhabitants
    """
    return mf_average_occupancy_per_unit() * mf_stock_of_units() + sf_average_occupancy_per_unit(
    ) * sf_stock_of_units()


integ_landuse4_nitrogen = functions.Integ(lambda: landuse4_daily_nitrogen(), lambda: 0)


@cache('step')
def wtw_total_calcium_hydroxide_ghg():
    """
    Real Name: WTW Total Calcium Hydroxide GHG
    Original Eqn: WTW Total Calcium Hydroxide*WTW Unit Calcium Hydroxide GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wtw_total_calcium_hydroxide() * wtw_unit_calcium_hydroxide_ghg()


@cache('run')
def bioretention_acceptability():
    """
    Real Name: Bioretention Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('run')
def lm_annual_maintenance():
    """
    Real Name: LM Annual Maintenance
    Original Eqn: 15000
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 15000


@cache('run')
def gwp_annual_maintenance():
    """
    Real Name: GWP Annual Maintenance
    Original Eqn: 0
    Units: $
    Limits: (None, None)
    Type: constant

    Percentage of Initial Costs
    """
    return 0


@cache('step')
def bioswale_lcc():
    """
    Real Name: Bioswale LCC
    Original Eqn: INTEG ( Bioswale Daily Costs, Bioswale Design and Capital Costs*Bioswale Footprint)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_bioswale_lcc()


@cache('run')
def rwh_acceptability():
    """
    Real Name: RWH Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


integ_wwp_total_energy = functions.Integ(lambda: wwp_daily_energy(), lambda: 0)


@cache('step')
def bioswale_daily_costs():
    """
    Real Name: Bioswale Daily Costs
    Original Eqn: Bioswale Annual Maintenance Costs*Bioswale Footprint
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return bioswale_annual_maintenance_costs() * bioswale_footprint()


@cache('run')
def wdm_total_length_m1():
    """
    Real Name: WDM Total Length M1
    Original Eqn: 4500
    Units: m
    Limits: (None, None)
    Type: constant

    Length of Stormwater System
    """
    return 4500


@cache('run')
def green_roof_footprint():
    """
    Real Name: Green Roof Footprint
    Original Eqn: 10000
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 10000


@cache('run')
def mf_clothes_washer_demand():
    """
    Real Name: MF Clothes Washer Demand
    Original Eqn: 22
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 22


@cache('run')
def cc_upper_vc():
    """
    Real Name: CC Upper VC
    Original Eqn: 0.8
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 0.8


@cache('run')
def asphalt_cc_unit_cost():
    """
    Real Name: Asphalt CC Unit Cost
    Original Eqn: 1500
    Units: $/m2
    Limits: (None, None)
    Type: constant

    Construction and installation costs for 1m2 of regular pavement
    """
    return 1500


@cache('run')
def bioretention_flexibility_and_adaptability():
    """
    Real Name: Bioretention Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def unit_irrigation_demand():
    """
    Real Name: Unit Irrigation Demand
    Original Eqn: 12
    Units: L/(Day*m2)
    Limits: (None, None)
    Type: constant

    Water Resources Engineering, Larry Mays, 2001 (Table 11.1.5 Page 347)\t\tWatering 750m2 Lawn (7600 - 16000 L/Month)
    """
    return 12


@cache('step')
def utility_months():
    """
    Real Name: Utility Months
    Original Eqn: INTEGER(Time/30.5)
    Units: Month
    Limits: (None, None)
    Type: component


    """
    return int(time() / 30.5)


@cache('run')
def wwp_pump_efficiency():
    """
    Real Name: WWP Pump Efficiency
    Original Eqn: 93
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Pump Efficiency [%]
    """
    return 93


@cache('step')
def wwcs_lc_embodied_ghg():
    """
    Real Name: WWCS LC Embodied GHG
    Original Eqn: INTEG ( WWCS Maintenance GHG, WWCS Construction GHG M1+WWCS Construction GHG M2)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_wwcs_lc_embodied_ghg()


@cache('step')
def landuse3_nitrogen():
    """
    Real Name: Landuse3 Nitrogen
    Original Eqn: INTEG ( Landuse3 Daily Nitrogen, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_landuse3_nitrogen()


integ_wsc_total_costs = functions.Integ(
    lambda: wsc_running_costs(), lambda: wsc_construction() + wsc_disposal() + wsc_replacement())

integ_green_roof_runoff_total = functions.Integ(lambda: green_roof_runoff_daily(), lambda: 0)


@cache('run')
def green_roof_design_and_capital_costs():
    """
    Real Name: Green Roof Design and Capital Costs
    Original Eqn: 4000
    Units: $/m2
    Limits: (None, None)
    Type: constant

    TRCA Cost Tool
    """
    return 4000


@cache('run')
def wtw_unit_carbon_dioxide():
    """
    Real Name: WTW Unit Carbon Dioxide
    Original Eqn: 0.03393
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.03393


@cache('run')
def swp_construction_and_installation():
    """
    Real Name: SWP Construction and Installation
    Original Eqn: 150000
    Units: $
    Limits: (None, None)
    Type: constant

    Installation Costs in $
    """
    return 150000


@cache('step')
def qh():
    """
    Real Name: Qh
    Original Eqn: IF THEN ELSE( Rainfall < 0.2*S , 0 , ((Rainfall-0.2*S)^2)/(Rainfall+0.8*S) )
    Units: mm
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(rainfall() < 0.2 * s(), 0,
                                  ((rainfall() - 0.2 * s())**2) / (rainfall() + 0.8 * s()))


@cache('step')
def cn_composite():
    """
    Real Name: CN Composite
    Original Eqn: INTEGER(((Landuse1*CN1)+(Landuse2*CN2)+(Landuse3*CN3)+(Landuse4*CN4)+(Green Roof Footprint\\ *Green Roof CN Value)+(Bioretention Footprint *Bioretention CN Value)+(Bioswale Footprint*Bioswale CN Value)+(RB and Cistern Footprint\\ * RB and Cistern CN Value)+ (PP CN Value * PP Footprint))/(Landuse1 + Landuse2 + Landuse3\\ + Landuse4 + Green Roof Footprint + Bioretention Footprint + Bioswale Footprint + \\ RB and Cistern Footprint + PP Footprint ))
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Composite CN number for 4 types of Landuse and different types of LIDs
    """
    return int(((landuse1() * cn1()) + (landuse2() * cn2()) + (landuse3() * cn3()) +
                (landuse4() * cn4()) + (green_roof_footprint() * green_roof_cn_value()) +
                (bioretention_footprint() * bioretention_cn_value()) +
                (bioswale_footprint() * bioswale_cn_value()) +
                (rb_and_cistern_footprint() * rb_and_cistern_cn_value()) +
                (pp_cn_value() * pp_footprint())) /
               (landuse1() + landuse2() + landuse3() + landuse4() + green_roof_footprint() +
                bioretention_footprint() + bioswale_footprint() + rb_and_cistern_footprint() +
                pp_footprint()))


@cache('step')
def wwtw_total_nitric_acid():
    """
    Real Name: WWTW Total Nitric Acid
    Original Eqn: INTEG ( Treated Wastewater*WWTW Unit Nitric Acid, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wwtw_total_nitric_acid()


@cache('step')
def schools_demand_variation_coefficient():
    """
    Real Name: Schools Demand Variation Coefficient
    Original Eqn: WITH LOOKUP ( Months, ([(0,0)-(12,2)],(0,1),(1,1.1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,0.25),(8,0.3),(9,1),\\ (10,1),(11,1),(12,1) ))
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(months(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                            [1, 1.1, 1, 1, 1, 1, 1, 0.25, 0.3, 1, 1, 1, 1])


@cache('run')
def wsc_construction():
    """
    Real Name: WSC Construction
    Original Eqn: 100
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 100


@cache('run')
def wtw_unit_polyaluminium_chloride_emenergy():
    """
    Real Name: WTW Unit Polyaluminium Chloride EmEnergy
    Original Eqn: 2.79
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 2.79


@cache('step')
def wsc_total_costs():
    """
    Real Name: WSC Total Costs
    Original Eqn: INTEG ( WSC Running Costs, WSC Construction+WSC Disposal+WSC Replacement)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_wsc_total_costs()


@cache('run')
def swtw_reliability():
    """
    Real Name: SWTW Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('step')
def utility_years():
    """
    Real Name: Utility Years
    Original Eqn: INTEGER (Utility Months/12)
    Units: Year
    Limits: (None, None)
    Type: component


    """
    return int(utility_months() / 12)


@cache('step')
def landuse1_daily_nitrogen():
    """
    Real Name: Landuse1 Daily Nitrogen
    Original Eqn: Landuse1 EMC Nitrogen*Landuse1 Percentage*Qv
    Units: mg/L
    Limits: (None, None)
    Type: component


    """
    return landuse1_emc_nitrogen() * landuse1_percentage() * qv()


@cache('run')
def wdm_unit_weight_m1():
    """
    Real Name: WDM Unit Weight M1
    Original Eqn: 1300
    Units: kg/m
    Limits: (None, None)
    Type: constant

    Unit Weight of 1m' of Material (PVC, PE, Mild Steel, Concrete, etc)
    """
    return 1300


@cache('run')
def wdm_unit_weight_m2():
    """
    Real Name: WDM Unit Weight M2
    Original Eqn: 10
    Units: kg/m
    Limits: (None, None)
    Type: constant

    Material 2
    """
    return 10


@cache('run')
def wwcs_unit_construction_energy_m1():
    """
    Real Name: WWCS Unit Construction Energy M1
    Original Eqn: 0.9
    Units: KWh/kg
    Limits: (None, None)
    Type: constant

    Embodied Energy for different categories of materials used for Stormwater \n    \t\tSystem. Table Appendix A WaterMet2
    """
    return 0.9


@cache('run')
def wastewater_generation_as_a_percentage_of_water_use():
    """
    Real Name: Wastewater Generation as a percentage of water use
    Original Eqn: 0.9
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Percentage of Distributed Drininkg Water Generated Waste
    """
    return 0.9


@cache('run')
def cn2():
    """
    Real Name: CN2
    Original Eqn: 78
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 78


@cache('run')
def wwp_duration_of_pump_operation():
    """
    Real Name: WWP Duration of Pump Operation
    Original Eqn: 12
    Units: Hours
    Limits: (None, None)
    Type: constant

    Number of Hours for Pump Operations (Assumption is 24 hours)
    """
    return 12


@cache('step')
def green_roof_percentage():
    """
    Real Name: Green Roof Percentage
    Original Eqn: (100*Green Roof Footprint)/LU Sum
    Units: Percentage
    Limits: (None, None)
    Type: component


    """
    return (100 * green_roof_footprint()) / lu_sum()


@cache('run')
def swcs_unit_maintenance_energy_m2():
    """
    Real Name: SWCS Unit Maintenance Energy M2
    Original Eqn: 0.05
    Units: KWh/m
    Limits: (None, None)
    Type: constant


    """
    return 0.05


@cache('step')
def dem_community_centers():
    """
    Real Name: Dem Community Centers
    Original Eqn: CC Area*Community Center Demand Variation Coefficient*CC Unit Demand
    Units: L/Day
    Limits: (None, None)
    Type: component


    """
    return cc_area() * community_center_demand_variation_coefficient() * cc_unit_demand()


@cache('run')
def wtw_unit_carbon_dioxide_emenergy():
    """
    Real Name: WTW Unit Carbon Dioxide EmEnergy
    Original Eqn: 1.4
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 1.4


integ_result_reached_system_capacity = functions.Integ(lambda: days_with_higher_demand(),
                                                       lambda: 0)


@cache('run')
def mf_wec_toilet():
    """
    Real Name: MF WEC Toilet
    Original Eqn: 1
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Water Efficiency Coefficient - Random
    """
    return 1


@cache('run')
def wwcs_annual_maintenance():
    """
    Real Name: WWCS Annual Maintenance
    Original Eqn: 1.05
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 1.05


@cache('run')
def swp_unit_conversion_factor():
    """
    Real Name: SWP Unit Conversion Factor
    Original Eqn: 101.9
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 101.9


@cache('step')
def sf_total_area_for_irrigation():
    """
    Real Name: SF Total Area for Irrigation
    Original Eqn: SF Lawn Area * SF Units Total Area Occupied
    Units: m2
    Limits: (None, None)
    Type: component


    """
    return sf_lawn_area() * sf_units_total_area_occupied()


@cache('step')
def ob_demand_variation_coefficient():
    """
    Real Name: OB Demand Variation Coefficient
    Original Eqn: RANDOM UNIFORM( OB Lower VC , OB Upper VC , 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.random_uniform(ob_lower_vc(), ob_upper_vc(), 1)


@cache('step')
def wtw_total_polyaluminium_chloride_ghg():
    """
    Real Name: WTW Total Polyaluminium Chloride GHG
    Original Eqn: INTEG ( WTW Total Polyaluminium Chloride*WTW Unit Polyaluimium Chloride GHG, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_total_polyaluminium_chloride_ghg()


@cache('run')
def wtm_disposal():
    """
    Real Name: WTM Disposal
    Original Eqn: 1.2
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 1.2


@cache('run')
def wdm_unit_construction_energy_m2():
    """
    Real Name: WDM Unit Construction Energy M2
    Original Eqn: 0.9
    Units: KWh/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.9


@cache('run')
def wdm_unit_construction_energy_m1():
    """
    Real Name: WDM Unit Construction Energy M1
    Original Eqn: 0.9
    Units: KWh/kg
    Limits: (None, None)
    Type: constant

    Embodied Energy for different categories of materials used for Stormwater \n    \t\tSystem. Table Appendix A WaterMet2
    """
    return 0.9


@cache('run')
def ia_percentage_of_area_collected():
    """
    Real Name: IA Percentage of Area Collected
    Original Eqn: 0.65
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Percentage of Total Impervious Areas Collected Rainwater (Assumption)
    """
    return 0.65


@cache('step')
def result_treatment_lcc():
    """
    Real Name: Result Treatment LCC
    Original Eqn: WTW Total Costs+WWTW Total Costs + SWTW Total Costs
    Units: $
    Limits: (None, None)
    Type: component


    """
    return wtw_total_costs() + wwtw_total_costs() + swtw_total_costs()


@cache('step')
def wwtw_total_ferric_sulphate_ghg():
    """
    Real Name: WWTW Total Ferric Sulphate GHG
    Original Eqn: WWTW Total Ferric Sulphate*WWTW Unit Ferric Sulphate GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_ferric_sulphate() * wwtw_unit_ferric_sulphate_ghg()


@cache('run')
def wtw_unit_polyaluminium_chloride():
    """
    Real Name: WTW Unit Polyaluminium Chloride
    Original Eqn: 0.02886
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.02886


integ_landuse3_nitrogen = functions.Integ(lambda: landuse3_daily_nitrogen(), lambda: 0)


@cache('run')
def wtw_reliability():
    """
    Real Name: WTW Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def bioretention_cn_value():
    """
    Real Name: Bioretention CN Value
    Original Eqn: 45
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 45


@cache('run')
def lm_percentage_of_hospitals():
    """
    Real Name: LM Percentage of Hospitals
    Original Eqn: 0.42
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.42


@cache('run')
def wwp_risk_to_human_health():
    """
    Real Name: WWP Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('step')
def restaurants_demand_variation_coefficient():
    """
    Real Name: Restaurants Demand Variation Coefficient
    Original Eqn: RANDOM UNIFORM( Restaurants Lower VC , Restaurants Upper VC , 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.random_uniform(restaurants_lower_vc(), restaurants_upper_vc(), 1)


integ_gwp_total_lcc = functions.Integ(
    lambda: gwp_daily_costs(),
    lambda: (gwp_construction_and_installation()) * gwp_number_of_pumps())


@cache('run')
def wtw_electricity_for_treatment_of_m3():
    """
    Real Name: WTW Electricity for treatment of m3
    Original Eqn: 1.2
    Units: KWh/m3
    Limits: (None, None)
    Type: constant

    Energy required for treatment of 1m3 of drinking water
    """
    return 1.2


@cache('step')
def landuse4_daily_nitrogen():
    """
    Real Name: Landuse4 Daily Nitrogen
    Original Eqn: Landuse4 EMC Nitrogen*Landuse4 Percentage*Qv
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return landuse4_emc_nitrogen() * landuse4_percentage() * qv()


@cache('step')
def wdm_total_weight_m2():
    """
    Real Name: WDM Total Weight M2
    Original Eqn: WDM Total Length M2*WDM Unit Weight M2
    Units: kg
    Limits: (None, None)
    Type: component

    Weight in Killograms for Material 2
    """
    return wdm_total_length_m2() * wdm_unit_weight_m2()


@cache('step')
def wdm_total_weight_m1():
    """
    Real Name: WDM Total Weight M1
    Original Eqn: WDM Total Length M1*WDM Unit Weight M1
    Units: kg
    Limits: (None, None)
    Type: component

    Total Weight of Stormwater System (in Killograms)
    """
    return wdm_total_length_m1() * wdm_unit_weight_m1()


@cache('run')
def swp_motor_efficiency():
    """
    Real Name: SWP Motor Efficiency
    Original Eqn: 80
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Motor Efficiency [%]
    """
    return 80


@cache('run')
def wtw_number_of_staff():
    """
    Real Name: WTW Number of Staff
    Original Eqn: 15
    Units: Persons
    Limits: (2.0, 100.0)
    Type: constant

    Number of Staff Required for WTW Operation
    """
    return 15


@cache('run')
def rr_unit_ghg_urea():
    """
    Real Name: RR Unit GHG Urea
    Original Eqn: 1.52
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 1.52


@cache('run')
def wwp_price_per_kwh():
    """
    Real Name: WWP Price per kWh
    Original Eqn: 0.11
    Units: $/KWh
    Limits: (0.0, 1.0)
    Type: constant

    Price of Energy (Dollars/Kwh)
    """
    return 0.11


@cache('run')
def wtw_flexibility_and_adaptability():
    """
    Real Name: WTW Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


integ_gwp_total_ghg_emission = functions.Integ(lambda: gwp_daily_ghg_emissions(), lambda: 0)


@cache('run')
def porous_pavement_affordability():
    """
    Real Name: Porous Pavement Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('step')
def lm_inflow_total():
    """
    Real Name: LM Inflow Total
    Original Eqn: IF THEN ELSE( (LM Inflow Hospitals+LM Inflow Office Buildings+LM Inflow Schools)>LM Maximum Daily Capacity\\ , LM Maximum Daily Capacity , (LM Inflow Hospitals+LM Inflow Office Buildings+LM Inflow Schools\\ ) )
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(
        (lm_inflow_hospitals() + lm_inflow_office_buildings() + lm_inflow_schools()) >
        lm_maximum_daily_capacity(), lm_maximum_daily_capacity(),
        (lm_inflow_hospitals() + lm_inflow_office_buildings() + lm_inflow_schools()))


@cache('run')
def wwp_annual_maintenance():
    """
    Real Name: WWP Annual Maintenance
    Original Eqn: 10000
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Annual Costs for Maintenance
    """
    return 10000


@cache('run')
def unit_demand_per_bed():
    """
    Real Name: Unit Demand per Bed
    Original Eqn: 1310
    Units: L/Day*Bed
    Limits: (None, None)
    Type: constant


    """
    return 1310


integ_swcs_lc_energy_embodied = functions.Integ(
    lambda: swcs_emenergy_maintenance(),
    lambda: swcs_construction_energy_m1() + swcs_construction_energy_m2())

integ_lm_total_energy = functions.Integ(lambda: lm_daily_energy_consumption(), lambda: 0)


@cache('run')
def rb_and_cistern_cn_value():
    """
    Real Name: RB and Cistern CN Value
    Original Eqn: 85
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    LTHIA-LID
    """
    return 85


integ_wwtw_total_costs = functions.Integ(
    lambda: wwtw_running_costs(),
    lambda: (wwtw_construction_and_installation() + wwtw_capital_investment()) * 1e+006)


@cache('step')
def lm_daily_energy_consumption():
    """
    Real Name: LM Daily Energy Consumption
    Original Eqn: LM Inflow Total*LM kWh per m3
    Units: KWh/Day
    Limits: (None, None)
    Type: component


    """
    return lm_inflow_total() * lm_kwh_per_m3()


@cache('run')
def swp_space_requirements():
    """
    Real Name: SWP Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def wwtw_treated_wastewater():
    """
    Real Name: WWTW Treated Wastewater
    Original Eqn: Treated Wastewater
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return treated_wastewater()


@cache('step')
def rr_daily_biogas():
    """
    Real Name: RR Daily Biogas
    Original Eqn: RR Unit Biogas*Wastewater Treated
    Units: m3
    Limits: (None, None)
    Type: component


    """
    return rr_unit_biogas() * wastewater_treated()


@cache('run')
def mf_wec_dishwasher():
    """
    Real Name: MF WEC Dishwasher
    Original Eqn: 1
    Units: Percentage
    Limits: (None, None)
    Type: constant

    Water Efficiency Coefficient - Random
    """
    return 1


@cache('step')
def swt_total_ferric_chloride_ghg():
    """
    Real Name: SWT Total Ferric Chloride GHG
    Original Eqn: SWT Ferric Chloride*SWT Unit Ferric Chloride GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return swt_ferric_chloride() * swt_unit_ferric_chloride_ghg()


integ_landuse1_nitrogen = functions.Integ(lambda: landuse1_daily_nitrogen(), lambda: 0)


@cache('step')
def wwcs_lc_embodied_energy():
    """
    Real Name: WWCS LC Embodied Energy
    Original Eqn: INTEG ( WWCS EmEnergy Maintenance, WWCS Construction Energy M1 + WWCS Construction Energy M2)
    Units: KWh
    Limits: (None, None)
    Type: component

    Total Energy(kwh) required for SWS construction and maintenance\t\tInitial Value = Construction
    """
    return integ_wwcs_lc_embodied_energy()


@cache('run')
def ob_unit_demand_per_m2():
    """
    Real Name: OB Unit Demand per m2
    Original Eqn: 4.2
    Units: L/(Day*m2)
    Limits: (None, None)
    Type: constant

    Source: Water Resources Engineering, Larry W Mays, 2001 (Table 11.1.4. Page 346)\t\tWater Distribution System Design PPT
    """
    return 4.2


@cache('run')
def sf_wec_faucet():
    """
    Real Name: SF WEC Faucet
    Original Eqn: 0.8
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.8


@cache('run')
def restaurants_upper_vc():
    """
    Real Name: Restaurants Upper VC
    Original Eqn: 1.21
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 1.21


integ_wp_total_lcc = functions.Integ(lambda: wp_daily_costs(),
                                     lambda: wp_construction_and_installation())


@cache('step')
def mf_wd_per_capita_no_measures():
    """
    Real Name: MF WD per Capita No Measures
    Original Eqn: (MF Bathtub Demand + MF Clothes Washer Demand + MF Dishwasher Demand + MF Faucet Demand\\ + MF Leaks + MF Shower Demand + MF Toilet Demand)*MF Coefficient of Seasonal Variation
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: component


    """
    return (mf_bathtub_demand() + mf_clothes_washer_demand() + mf_dishwasher_demand() +
            mf_faucet_demand() + mf_leaks() + mf_shower_demand() +
            mf_toilet_demand()) * mf_coefficient_of_seasonal_variation()


@cache('run')
def rr_unit_ammonium_nitrate():
    """
    Real Name: RR Unit Ammonium Nitrate
    Original Eqn: 20
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 20


@cache('run')
def cn4():
    """
    Real Name: CN4
    Original Eqn: 45
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 45


@cache('run')
def swcs_disposal():
    """
    Real Name: SWCS Disposal
    Original Eqn: 0
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('run')
def lm_space_requirements():
    """
    Real Name: LM Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def cn3():
    """
    Real Name: CN3
    Original Eqn: 74
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 74


@cache('run')
def cn1():
    """
    Real Name: CN1
    Original Eqn: 70
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 70


integ_wwtw_operation_ghg = functions.Integ(
    lambda: wwtw_operation_electricity() * ghg_emission_generation_electricity_factor(), lambda: 0)


@cache('step')
def months():
    """
    Real Name: Months
    Original Eqn: Months Counter + 1
    Units: Month
    Limits: (None, None)
    Type: component


    """
    return months_counter() + 1


@cache('step')
def wwtw_embodied_ghg_for_chemicals():
    """
    Real Name: WWTW Embodied GHG for Chemicals
    Original Eqn: INTEG ( WWTW Total Calcium Hydroxide GHG+WWTW Total Ethanol GHG+WWTW Total Ferric Chloride GHG\\ +WWTW Total Ferric Sulphate GHG+WWTW Total Methanol GHG+WWTW Total Nitric Acid GHG, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_wwtw_embodied_ghg_for_chemicals()


@cache('step')
def rh_tank_current_storage_volume():
    """
    Real Name: RH Tank Current Storage Volume
    Original Eqn: INTEG ( RH Tank Inflow-RH Tank Outflow, 0)
    Units: m3
    Limits: (None, None)
    Type: component

    Ovde ubaciti napredan Operational Model Preko Control Variable
    """
    return integ_rh_tank_current_storage_volume()


@cache('run')
def mf_average_occupancy_per_unit():
    """
    Real Name: MF Average Occupancy per Unit
    Original Eqn: 1.9
    Units: Persons
    Limits: (None, None)
    Type: constant

    Average number of persons living in a single family household unit
    """
    return 1.9


@cache('step')
def wwp_total_ghg_emission():
    """
    Real Name: WWP Total GHG Emission
    Original Eqn: INTEG ( WWP Daily GHG Emissions, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_wwp_total_ghg_emission()


@cache('run')
def gws_flexibility_and_adaptability():
    """
    Real Name: GWS Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def swcs_number_of_maintenance_trips():
    """
    Real Name: SWCS Number of Maintenance Trips
    Original Eqn: 2/Days in a Year
    Units: Number
    Limits: (None, None)
    Type: component

    Number of Trips Per Year
    """
    return 2 / days_in_a_year()


@cache('step')
def lu_sum():
    """
    Real Name: LU Sum
    Original Eqn: Landuse1+Landuse2+Landuse3+Landuse4+Green Roof Footprint+Bioretention Footprint+Bioswale Footprint\\ +RB and Cistern Footprint+PP Footprint
    Units: m2
    Limits: (None, None)
    Type: component

    Sum of all Ladnuse areas to calculate proportion (%) of particular landuse
    """
    return landuse1() + landuse2() + landuse3() + landuse4() + green_roof_footprint(
    ) + bioretention_footprint() + bioswale_footprint() + rb_and_cistern_footprint(
    ) + pp_footprint()


@cache('step')
def result_rr_lcc():
    """
    Real Name: Result RR LCC
    Original Eqn: RHP Total LCC + GWP Total LCC + GWS Total LCC + LM Total LCC
    Units: $
    Limits: (None, None)
    Type: component


    """
    return rhp_total_lcc() + gwp_total_lcc() + gws_total_lcc() + lm_total_lcc()


@cache('step')
def result_pumping_lcc():
    """
    Real Name: Result Pumping LCC
    Original Eqn: SWP Total LCC+WP Total LCC+WWP Total LCC
    Units: $
    Limits: (None, None)
    Type: component


    """
    return swp_total_lcc() + wp_total_lcc() + wwp_total_lcc()


@cache('run')
def wtw_unit_calcium_hydroxide_ghg():
    """
    Real Name: WTW Unit Calcium Hydroxide GHG
    Original Eqn: 0.794
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 0.794


@cache('run')
def sf_rate_of_adoption():
    """
    Real Name: SF Rate of Adoption
    Original Eqn: 0.55
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.55


@cache('run')
def swp_affordability():
    """
    Real Name: SWP Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('run')
def mbr_kwh_per_m3():
    """
    Real Name: MBR kWh per m3
    Original Eqn: 4.5
    Units: KWh/m3
    Limits: (None, None)
    Type: constant

    Figure 3. LCA results for the decentralized LM treatment and water reuse \n    \t\tsystem. (a) Annualized results for the analysis period (25 years) for the \n    \t\tentire system per ML of influent that is treated and recycled. - System \n    \t\tMaterials, Settling Tank Emissions, Pumping, Treatment
    """
    return 4.5


@cache('run')
def rwh_risk_to_human_health():
    """
    Real Name: RWH Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('step')
def result_network_lcc():
    """
    Real Name: Result Network LCC
    Original Eqn: SWCS Total Costs+WDM Total Costs+WSC Total Costs+WTM Total Costs+WWCS Total Costs
    Units: $
    Limits: (None, None)
    Type: component


    """
    return swcs_total_costs() + wdm_total_costs() + wsc_total_costs() + wtm_total_costs(
    ) + wwcs_total_costs()


@cache('step')
def swcs_construction_energy_m2():
    """
    Real Name: SWCS Construction Energy M2
    Original Eqn: SWCS Total Weight M2*SWCS Unit Construction Energy M2
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return swcs_total_weight_m2() * swcs_unit_construction_energy_m2()


@cache('run')
def bioretention_footprint():
    """
    Real Name: Bioretention Footprint
    Original Eqn: 500
    Units: m2
    Limits: (None, None)
    Type: constant


    """
    return 500


@cache('step')
def swcs_construction_energy_m1():
    """
    Real Name: SWCS Construction Energy M1
    Original Eqn: SWCS Total Weight M1*SWCS Unit Construction Energy M1
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return swcs_total_weight_m1() * swcs_unit_construction_energy_m1()


@cache('run')
def wtw_affordability():
    """
    Real Name: WTW Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0, 1.0)
    Type: constant


    """
    return 1


@cache('run')
def wtw_capital_investment():
    """
    Real Name: WTW Capital Investment
    Original Eqn: 25.7
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 25.7


@cache('run')
def swtw_space_requirements():
    """
    Real Name: SWTW Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def swp_daily_ghg_emissions():
    """
    Real Name: SWP Daily GHG Emissions
    Original Eqn: SWP Daily Energy*WP CO2 per kWh
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return swp_daily_energy() * wp_co2_per_kwh()


@cache('step')
def wwcs_number_of_maintenance_trips():
    """
    Real Name: WWCS Number of Maintenance Trips
    Original Eqn: 2/Days in a Year
    Units: Number
    Limits: (None, None)
    Type: component

    Number of Trips Per Year
    """
    return 2 / days_in_a_year()


@cache('step')
def lm_daily_ghg_emission():
    """
    Real Name: LM Daily GHG Emission
    Original Eqn: LM GHG per m3*LM Inflow Total
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return lm_ghg_per_m3() * lm_inflow_total()


@cache('step')
def wtw_total_alum_ghg():
    """
    Real Name: WTW Total Alum GHG
    Original Eqn: WTW Unit Alum GHG*WTW Total Alum
    Units: kgCO2eq
    Limits: (None, None)
    Type: component

    Total GHG emissions for Alum used in WTW
    """
    return wtw_unit_alum_ghg() * wtw_total_alum()


integ_wtm_total_costs = functions.Integ(
    lambda: wtm_running_costs(), lambda: wtm_construction() + wtm_disposal() + wtm_replacement())


@cache('step')
def wwtw_total_methanol_emenergy():
    """
    Real Name: WWTW Total Methanol EmEnergy
    Original Eqn: WWTW Total Methanol*WWTW Unit Methanol EmEnergy
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_methanol() * wwtw_unit_methanol_emenergy()


@cache('step')
def landuse3_percentage():
    """
    Real Name: Landuse3 Percentage
    Original Eqn: (100*Landuse3)/LU Sum
    Units: Percentage
    Limits: (None, None)
    Type: component


    """
    return (100 * landuse3()) / lu_sum()


@cache('run')
def wp_risk_to_human_health():
    """
    Real Name: WP Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0, 1.0)
    Type: constant


    """
    return 4


@cache('run')
def rwh_affordability():
    """
    Real Name: RWH Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('step')
def result_lid_lcc():
    """
    Real Name: Result LID LCC
    Original Eqn: Bioswale LCC + Biretention LCC + Green Roof LCC + PP LCC + RB and Cistern LCC
    Units: $
    Limits: (None, None)
    Type: component


    """
    return bioswale_lcc() + biretention_lcc() + green_roof_lcc() + pp_lcc() + rb_and_cistern_lcc()


@cache('step')
def landuse1_percentage():
    """
    Real Name: Landuse1 Percentage
    Original Eqn: (100*Landuse1)/LU Sum
    Units: Percentage
    Limits: (None, None)
    Type: component


    """
    return (100 * landuse1()) / lu_sum()


@cache('step')
def lm_inflow_hospitals():
    """
    Real Name: LM Inflow Hospitals
    Original Eqn: Dem Hospitals*Dem Hospitals Restroom*LM Percentage of Hospitals
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return dem_hospitals() * dem_hospitals_restroom() * lm_percentage_of_hospitals()


@cache('run')
def wtw_available_capacity():
    """
    Real Name: WTW Available Capacity
    Original Eqn: 0.35
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.35


integ_wwtw_embodied_ghg_for_chemicals = functions.Integ(lambda: wwtw_total_calcium_hydroxide_ghg()+wwtw_total_ethanol_ghg()+wwtw_total_ferric_chloride_ghg()+wwtw_total_ferric_sulphate_ghg()+wwtw_total_methanol_ghg()+wwtw_total_nitric_acid_ghg(), lambda: 0)


@cache('step')
def wdm_lc_embodied_energy():
    """
    Real Name: WDM LC Embodied Energy
    Original Eqn: INTEG ( WDM EmEnergy Maintenance, WDM Construction Energy M1 + WDM Construction Energy M2)
    Units: KWh
    Limits: (None, None)
    Type: component

    Total Energy(kwh) required for SWS construction and maintenance\t\tInitial Value = Construction
    """
    return integ_wdm_lc_embodied_energy()


@cache('run')
def mf_shower_demand():
    """
    Real Name: MF Shower Demand
    Original Eqn: 36
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: constant

    According to the Toronto\u2019s Design Criteria for Sewers and Watermains and \n    \t\tCity of Toronto Water User Breakdown Information, Keating Channel Precinct \n    \t\tEnv. Study Report
    """
    return 36


@cache('step')
def gws_total_installation_and_construction_costs():
    """
    Real Name: GWS Total Installation and Construction Costs
    Original Eqn: GWS Installation Costs * GWS Total Volume
    Units: $
    Limits: (None, None)
    Type: component


    """
    return gws_installation_costs() * gws_total_volume()


integ_gwp_total_energy = functions.Integ(lambda: gwp_daily_energy(), lambda: 0)


@cache('step')
def daily_water_demand():
    """
    Real Name: Daily Water Demand
    Original Eqn: (Commercial and Institutional Demand+Domestic Demand+Industrial Demand+Irrigation Demand\\ )*(1+Water Supply Leakage Rate)
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return (commercial_and_institutional_demand() + domestic_demand() + industrial_demand() +
            irrigation_demand()) * (1 + water_supply_leakage_rate())


@cache('step')
def result_system_affordability():
    """
    Real Name: Result System Affordability
    Original Eqn: Bioretention Affordability+Bioswale Affordability+Green Roof Affordability+GWS Affordability\\ +LM Affordability+MBR Affordability+Porous Pavement Affordability+RWH Affordability\\ +SWP Affordability+SWTW Affordability+WP Affordability+WTW Affordability+WWP Affordability\\ +WWTW Affordability
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return bioretention_affordability() + bioswale_affordability(
    ) + green_roof_affordability() + gws_affordability() + lm_affordability() + mbr_affordability(
    ) + porous_pavement_affordability() + rwh_affordability() + swp_affordability(
    ) + swtw_affordability() + wp_affordability() + wtw_affordability() + wwp_affordability(
    ) + wwtw_affordability()


@cache('run')
def wtw_construction_and_installation():
    """
    Real Name: WTW Construction and Installation
    Original Eqn: 0
    Units: $
    Limits: (None, None)
    Type: constant

    Construction Costs of Water Treatment Works
    """
    return 0


@cache('run')
def wtm_construction():
    """
    Real Name: WTM Construction
    Original Eqn: 15
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 15


@cache('run')
def sf_lawn_area():
    """
    Real Name: SF Lawn Area
    Original Eqn: 0.25
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Percentage of Lots as Lawn
    """
    return 0.25


@cache('run')
def sf_new_units_annually():
    """
    Real Name: SF New Units Annually
    Original Eqn: 3000
    Units: SF Units
    Limits: (None, None)
    Type: constant

    Number of single-family units added to the neighborhood annually
    """
    return 3000


@cache('run')
def wtw_unit_alum():
    """
    Real Name: WTW Unit Alum
    Original Eqn: 0.00166
    Units: kg/m3
    Limits: (None, None)
    Type: constant

    Alum required for treatment of 1m3 of water\t\tPage 83, Table 5.8
    """
    return 0.00166


@cache('step')
def industrial_demand_variation_coefficient():
    """
    Real Name: Industrial Demand Variation Coefficient
    Original Eqn: WITH LOOKUP ( Months, ([(0,0)-(12,13)],(0,1),(1,1.1),(2,1.2),(3,1.19),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1.1\\ ),(10,1.3),(11,1.25),(12,1.34) ))
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.lookup(months(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                            [1, 1.1, 1.2, 1.19, 1, 1, 1, 1, 1, 1.1, 1.3, 1.25, 1.34])


@cache('step')
def wdm_lc_embodied_ghg():
    """
    Real Name: WDM LC Embodied GHG
    Original Eqn: INTEG ( WDM Maintenance GHG, WDM Construction GHG M1+WDM Construction GHG M2)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_wdm_lc_embodied_ghg()


@cache('run')
def swcs_unit_maintenance_ghg_m1():
    """
    Real Name: SWCS Unit Maintenance GHG M1
    Original Eqn: 0.5
    Units: kgCO2eq/m
    Limits: (None, None)
    Type: constant

    Energy Report, Table 2.3
    """
    return 0.5


@cache('run')
def swcs_unit_maintenance_ghg_m2():
    """
    Real Name: SWCS Unit Maintenance GHG M2
    Original Eqn: 0.5
    Units: kgCO2eq/m
    Limits: (None, None)
    Type: constant


    """
    return 0.5


@cache('step')
def wastewater_generated():
    """
    Real Name: Wastewater Generated
    Original Eqn: (Distributed Treated Water - Irrigation Demand) * Wastewater Generation as a percentage of water use
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return (distributed_treated_water() -
            irrigation_demand()) * wastewater_generation_as_a_percentage_of_water_use()


@cache('step')
def wtw_total_microsand():
    """
    Real Name: WTW Total Microsand
    Original Eqn: INTEG ( Treated Water*WTW Unit Microsand, 0)
    Units: kg
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_total_microsand()


@cache('step')
def swcs_total_costs():
    """
    Real Name: SWCS Total Costs
    Original Eqn: INTEG ( SWCS Running Costs, SWCS Construction + SWCS Replacement + SWCS Disposal)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_swcs_total_costs()


@cache('step')
def landuse2_percentage():
    """
    Real Name: Landuse2 Percentage
    Original Eqn: (100*Landuse2)/LU Sum
    Units: Percentage
    Limits: (None, None)
    Type: component


    """
    return (100 * landuse2()) / lu_sum()


@cache('run')
def wdm_unit_construction_ghg_m1():
    """
    Real Name: WDM Unit Construction GHG M1
    Original Eqn: 2.36
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant

    GHG Emissions per kg of Pipe Materials, Appendix A
    """
    return 2.36


@cache('run')
def wdm_unit_construction_ghg_m2():
    """
    Real Name: WDM Unit Construction GHG M2
    Original Eqn: 2.36
    Units: kgCO2eq/kg
    Limits: (None, None)
    Type: constant


    """
    return 2.36


@cache('step')
def rhp_daily_ghg_emissions():
    """
    Real Name: RHP Daily GHG Emissions
    Original Eqn: RHP Daily Energy*WP CO2 per kWh
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return rhp_daily_energy() * wp_co2_per_kwh()


integ_rh_total_water_harvested = functions.Integ(lambda: rh_tank_inflow(), lambda: 0)


@cache('run')
def wtw_annual_maintenance():
    """
    Real Name: WTW Annual Maintenance
    Original Eqn: 2.5
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 2.5


@cache('run')
def wwtw_flexibility_and_adaptability():
    """
    Real Name: WWTW Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def wp_space_requirements():
    """
    Real Name: WP Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0, 1.0)
    Type: constant


    """
    return 2


@cache('step')
def wtw_operation_ghg():
    """
    Real Name: WTW Operation GHG
    Original Eqn: INTEG ( GHG Emission Generation Electricity Factor*WTW Operation Energy, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_wtw_operation_ghg()


@cache('step')
def wwtw_total_calcium_hydroxide_ghg():
    """
    Real Name: WWTW Total Calcium Hydroxide GHG
    Original Eqn: WWTW Total Calcium Hydroxide*WWTW Unit Calcium Hydroxide GHG
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return wwtw_total_calcium_hydroxide() * wwtw_unit_calcium_hydroxide_ghg()


@cache('run')
def wp_pump_efficiency():
    """
    Real Name: WP Pump Efficiency
    Original Eqn: 93
    Units: Dmnl
    Limits: (None, None)
    Type: constant

    Pump Efficiency [%]
    """
    return 93


@cache('run')
def swcs_replacement():
    """
    Real Name: SWCS Replacement
    Original Eqn: 0
    Units: $
    Limits: (None, None)
    Type: constant


    """
    return 0


@cache('step')
def coefficient_of_seasonal_variation_in_irrigation_demand():
    """
    Real Name: Coefficient of Seasonal Variation in Irrigation Demand
    Original Eqn: WITH LOOKUP ( Months, ([(0,0)-(12,2)],(1,0),(2,0),(3,0),(4,0.5),(5,1),(6,1.1),(7,1.25),(8,1.3),(9,1),(10,\\ 0),(11,0),(12,0) ))
    Units: Dmnl
    Limits: (None, None)
    Type: component

    Monthly and Daily Coefficient
    """
    return functions.lookup(months(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                            [0, 0, 0, 0.5, 1, 1.1, 1.25, 1.3, 1, 0, 0, 0])


@cache('step')
def distributed_treated_water():
    """
    Real Name: Distributed Treated Water
    Original Eqn: IF THEN ELSE( Daily Water Demand >= System Water Capacity , System Water Capacity , \\ Daily Water Demand )
    Units: m3/Day
    Limits: (None, None)
    Type: component


    """
    return functions.if_then_else(daily_water_demand() >= system_water_capacity(),
                                  system_water_capacity(), daily_water_demand())


@cache('run')
def wwtw_electricity_for_treatment_of_m3():
    """
    Real Name: WWTW Electricity for treatment of m3
    Original Eqn: 0.45
    Units: KWh/m3
    Limits: (None, None)
    Type: constant

    Energy required for treatment of 1m3 of wastewater, Table 5.3. Example\t\tTable 1, Toronto urban water metabolism, Emission factors for Toronto
    """
    return 0.45


@cache('run')
def sf_wec_toilet():
    """
    Real Name: SF WEC Toilet
    Original Eqn: 0.7
    Units: Percentage
    Limits: (None, None)
    Type: constant


    """
    return 0.7


@cache('step')
def sf_wd_per_capita_no_measures():
    """
    Real Name: SF WD per Capita No Measures
    Original Eqn: (SF Bathtub Demand+SF Clothes Washer Demand+SF Dishwasher Demand+SF Faucet Demand+SF Leaks\\ +SF Shower Demand+SF Toilet Demand +SF Other)*MF Coefficient of Seasonal Variation
    Units: L/(Day*cap)
    Limits: (None, None)
    Type: component


    """
    return (sf_bathtub_demand() + sf_clothes_washer_demand() + sf_dishwasher_demand() +
            sf_faucet_demand() + sf_leaks() + sf_shower_demand() + sf_toilet_demand() +
            sf_other()) * mf_coefficient_of_seasonal_variation()


@cache('run')
def wwp_reliability():
    """
    Real Name: WWP Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('step')
def swp_daily_energy():
    """
    Real Name: SWP Daily Energy
    Original Eqn: (SW Daily Rate * 0.0115741 * SWP Duration of Pump Operation * SWP Total Dynamic Head of Pump\\ * SWP Unit Conversion Factor) / (SWP Motor Efficiency * SWP Pump Efficiency * SWP Variable Speed Drive Efficiency\\ )
    Units: KWh/Day
    Limits: (None, None)
    Type: component

    Daily Energy Consumption required for Drinking Water Pumping\t\t* 0.0115741 Conversion factor m3/day in liters/second
    """
    return (
        sw_daily_rate() * 0.0115741 * swp_duration_of_pump_operation() *
        swp_total_dynamic_head_of_pump() * swp_unit_conversion_factor()) / (
            swp_motor_efficiency() * swp_pump_efficiency() * swp_variable_speed_drive_efficiency())


@cache('step')
def lm_total_ghg():
    """
    Real Name: LM Total GHG
    Original Eqn: INTEG ( LM Daily GHG Emission, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_lm_total_ghg()


@cache('step')
def mf_wd_per_capita_water_sensitive():
    """
    Real Name: MF WD per Capita Water Sensitive
    Original Eqn: (MF Bathtub Demand * MF WEC Bathtub + MF Clothes Washer Demand * MF WEC Clothes Washer\\ + MF Dishwasher Demand * MF WEC Dishwasher + MF Faucet Demand * MF WEC Faucet + MF Leaks * MF WEC Leaks + MF Shower Demand * MF WEC Shower\\ + MF Toilet Demand * MF WEC Toilet) * MF Coefficient of Seasonal Variation
    Units: L/Day
    Limits: (None, None)
    Type: component


    """
    return (mf_bathtub_demand() * mf_wec_bathtub() +
            mf_clothes_washer_demand() * mf_wec_clothes_washer() +
            mf_dishwasher_demand() * mf_wec_dishwasher() + mf_faucet_demand() * mf_wec_faucet() +
            mf_leaks() * mf_wec_leaks() + mf_shower_demand() * mf_wec_shower() +
            mf_toilet_demand() * mf_wec_toilet()) * mf_coefficient_of_seasonal_variation()


@cache('run')
def sf_initial_stock_of_units():
    """
    Real Name: SF Initial Stock of Units
    Original Eqn: 250
    Units: SF Units
    Limits: (None, None)
    Type: constant

    Initial number of single-family units in the neighborhood
    """
    return 250


integ_rr_total_urea_generated = functions.Integ(lambda: rr_daily_urea(), lambda: 0)


@cache('step')
def swtw_total_costs():
    """
    Real Name: SWTW Total Costs
    Original Eqn: INTEG ( SWTW Running Costs, (SWTW Construction and Installation + SWTW Capital Investment)*10^6)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_swtw_total_costs()


@cache('run')
def mbr_installation_and_construction_costs():
    """
    Real Name: MBR Installation and Construction Costs
    Original Eqn: 1.4e+006
    Units: $
    Limits: (None, None)
    Type: constant

    For 151 m3/day\t302 m3/day\t3785 m3/day
    """
    return 1.4e+006


@cache('run')
def swtw_unit_ferric_chloride():
    """
    Real Name: SWTW Unit Ferric Chloride
    Original Eqn: 0.0299
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.0299


@cache('run')
def porous_pavement_space_requirements():
    """
    Real Name: Porous Pavement Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def gws_risk_to_human_health():
    """
    Real Name: GWS Risk to Human Health
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def wwtw_unit_ethanol():
    """
    Real Name: WWTW Unit Ethanol
    Original Eqn: 0.0003
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.0003


@cache('step')
def wwtw_operation_ghg():
    """
    Real Name: WWTW Operation GHG
    Original Eqn: INTEG ( WWTW Operation Electricity*GHG Emission Generation Electricity Factor, 0)
    Units: kgCO2eq
    Limits: (None, None)
    Type: component


    """
    return integ_wwtw_operation_ghg()


@cache('run')
def wwtw_space_requirements():
    """
    Real Name: WWTW Space Requirements
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('step')
def wp_total_energy():
    """
    Real Name: WP Total Energy
    Original Eqn: INTEG ( WP Daily Energy, 0)
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return integ_wp_total_energy()


@cache('run')
def wdm_unit_maintenance_energy_m1():
    """
    Real Name: WDM Unit Maintenance Energy M1
    Original Eqn: 0.05
    Units: KWh/m
    Limits: (None, None)
    Type: constant

    Energy Report, Table 2.3
    """
    return 0.05


@cache('run')
def bioswale_flexibility_and_adaptability():
    """
    Real Name: Bioswale Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def wwtw_reliability():
    """
    Real Name: WWTW Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('run')
def rh_system_construction_ghg():
    """
    Real Name: RH System Construction GHG
    Original Eqn: 20.15
    Units: kgCO2eq/m3
    Limits: (None, None)
    Type: constant

    Table 2.3. Energy Consumption and CO2 Emissions Indicators for Drainage System \n    \t\tConstruction and Maintenance\t\tREPORT ON ENERGY 12 IN THE URBAN WATER CYCLE
    """
    return 20.15


@cache('run')
def wtw_unit_calcium_hydroxide():
    """
    Real Name: WTW Unit Calcium Hydroxide
    Original Eqn: 0.03341
    Units: kg/m3
    Limits: (None, None)
    Type: constant


    """
    return 0.03341


@cache('run')
def mbr_acceptability():
    """
    Real Name: MBR Acceptability
    Original Eqn: 3
    Units: Dmnl
    Limits: (None, None)
    Type: constant


    """
    return 3


@cache('step')
def community_center_demand_variation_coefficient():
    """
    Real Name: Community Center Demand Variation Coefficient
    Original Eqn: RANDOM UNIFORM( CC Lower VC , CC Upper VC , 1 )
    Units: Dmnl
    Limits: (None, None)
    Type: component


    """
    return functions.random_uniform(cc_lower_vc(), cc_upper_vc(), 1)


@cache('run')
def porous_pavement_reliability():
    """
    Real Name: Porous Pavement Reliability
    Original Eqn: 4
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 4


@cache('step')
def rb_and_cistern_lcc():
    """
    Real Name: RB and Cistern LCC
    Original Eqn: INTEG ( RB and Cistern Daily Costs, RB Design and Capital Costs * RB and Cistern Storage Volume)
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_rb_and_cistern_lcc()


@cache('run')
def swtw_affordability():
    """
    Real Name: SWTW Affordability
    Original Eqn: 1
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 1


@cache('step')
def wdm_construction_energy_m1():
    """
    Real Name: WDM Construction Energy M1
    Original Eqn: WDM Total Weight M1*WDM Unit Construction Energy M1
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wdm_total_weight_m1() * wdm_unit_construction_energy_m1()


@cache('step')
def wdm_construction_energy_m2():
    """
    Real Name: WDM Construction Energy M2
    Original Eqn: WDM Total Weight M2*WDM Unit Construction Energy M2
    Units: KWh
    Limits: (None, None)
    Type: component


    """
    return wdm_total_weight_m2() * wdm_unit_construction_energy_m2()


@cache('step')
def gws_total_lcc():
    """
    Real Name: GWS Total LCC
    Original Eqn: INTEG ( GWS Daily Maintenance, (GWS Plumbing Costs per m2 * GWS Plumbing Area)+GWS Total Installation and Construction Costs\\ )
    Units: $
    Limits: (None, None)
    Type: component


    """
    return integ_gws_total_lcc()


@cache('run')
def swtw_flexibility_and_adaptability():
    """
    Real Name: SWTW Flexibility and Adaptability
    Original Eqn: 2
    Units: Dmnl
    Limits: (1.0, 5.0)
    Type: constant


    """
    return 2


@cache('run')
def wwtw_sludge_generated():
    """
    Real Name: WWTW Sludge Generated
    Original Eqn: 0.091
    Units: kg/m3
    Limits: (None, None)
    Type: constant

    Sludge Generated per 1m3 of wastewater
    """
    return 0.091


@cache('step')
def months_counter():
    """
    Real Name: Months Counter
    Original Eqn: Utility Months - (Utility Years*12)
    Units: Month
    Limits: (None, None)
    Type: component


    """
    return utility_months() - (utility_years() * 12)


@cache('step')
def mf_coefficient_of_seasonal_variation():
    """
    Real Name: MF Coefficient of Seasonal Variation
    Original Eqn: WITH LOOKUP ( Months, ([(0,0)-(12,2)],(1,1.16),(2,1.02),(3,1),(4,1),(5,1),(6,1.13),(7,1.18),(8,1.16),(9,1\\ ),(10,1),(11,1.1),(12,1.12) ))
    Units: Dmnl
    Limits: (0.5, 2.0)
    Type: component

    Monthly coefficients to represent seasonal variations in residential water \n    \t\tdemand
    """
    return functions.lookup(months(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                            [1.16, 1.02, 1, 1, 1, 1.13, 1.18, 1.16, 1, 1, 1.1, 1.12])


@cache('step')
def pp_daily_costs():
    """
    Real Name: PP Daily Costs
    Original Eqn: (PP Annual Maintenance Costs * PP Footprint)/365.25
    Units: $/Day
    Limits: (None, None)
    Type: component


    """
    return (pp_annual_maintenance_costs() * pp_footprint()) / 365.25
