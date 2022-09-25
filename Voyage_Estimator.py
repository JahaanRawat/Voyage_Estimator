class Parent_FO:
    """
    Class for creating
    """

    def __init__(self, bal, lad, hea, heating, bia, ct, ldd, dib, ld_speed, bl_speed):
        self.Ballast = bal
        self.Laden = lad
        self.Heatup = hea
        self.Heating = heating
        self.Bunkering_Idle_Anchorage = bia
        self.Canal_Transit = ct
        self.Loading_Deinerting_Deballstring = ldd
        self.Discharging_Inerting_Ballasting = dib
        self.Laden_Speed = ld_speed
        self.Ballast_Speed = bl_speed


class Destinations:
    """:cvar"""

    def __init__(self, frm, to, type, miles, FO):
        self.From = frm
        self.To = to
        self.Type = type
        self.Miles = miles
        self.days = miles/(FO.Laden_Speed/24)
        self.FO = FO

    def get_FO_Value(self):
        """:cvar"""

        if self.Type == 'B':
            return self.days * self.FO.Ballast
        else:
            return self.days * self.FO.Laden


class Voy_Legs:
    """:cvar"""

    def __init__(self, d_bp, d_ct, d_ptl, d_ptd, d_dob, d_hu, d_h, FO):
        """:cvar"""
        self.Port_Time_Loading = d_ptl * FO.Loading_Deinerting_Deballstring
        self.Port_Time_Discharging = d_ptd * FO.Discharging_Inerting_Ballasting

    def get_FO_Value(self):
        """:cvar"""
        return self.Port_Time_Loading + self.Port_Time_Discharging


class Expenses:
    """:cvar"""

    def __init__(self, voyage_list, VL, FOp, DOc, DOp, lpc, dpc, dh, i, oc, cb, tc):
        days = 0
        total_FO = 0
        for v in voyage_list:
            days += v.days
            total_FO += v.get_FO_value
        total_FO + VL.get_FO_value()

        self.days = days
        self.FO = total_FO
        self.FO_DO_cost = self.FO * FOp + DOc * DOp
        self.Load_Port_Cost = lpc
        self.Dis_Port_Cost = dpc
        self.Daily_Hire_Rate = dh
        self.Total_Hire_Cost = self.days * self.Daily_Hire_Rate
        self.Insurance_Rate = i
        self.Total_Insurance = self.Insurance_Rate * self.days
        self.operating_costs = oc
        self.Total_Operating_Costs = self.operating_costs * self.days
        self.crew_bonus = cb
        self.Tank_Cleaning = tc

    def get_Total_Cost(self):
        return self.FO_DO_cost + self.Load_Port_Cost + self.Dis_Port_Cost + self.Total_Hire_Cost + self.Total_Insurance + self.Total_Operating_Costs + self.crew_bonus + self.Tank_Cleaning


def get_cost_per_tonne(amount, cost):
    return amount/cost


