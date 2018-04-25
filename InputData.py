import TransitionMatrix as TM
import scr.MarkovClasses as MarkovCls

POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15   # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 0.25         # years (length of time step, how frequently you look at the patient)
DISCOUNT = 0.03     # annual discount rate

# transition matrix

TRANS_MATRIX=[[None,TM.srroke_afterfirst,0,TM.death_afterfirst,TM.non_stroke_deathrate],
              [0,None,TM.rate_post_stroke,0,0],
              [0,TM.rate_poststr_stroke,None,TM.rate_poststr_strokedeath,TM.non_stroke_mortality],
              [0,0,0,None,0],
              [0,0,0,0,None]]
Prob_TransMatrix_None=MarkovCls.continuous_to_discrete(TRANS_MATRIX,DELTA_T)


TRANS_MATRIX_COMBO=[[None,TM.srroke_afterfirst,0,TM.death_afterfirst,TM.non_stroke_deathrate],
                    [0,None,TM.rate_post_stroke,0,0],
                    [0,TM.rate_poststr_stroke_withtherapy,None,TM.rate_poststr_strokedeath,TM.therapy_non_stroke_deathrate],
                    [0,0,0,None,0],
                    [0,0,0,0,None]]
Prob_TransMatrix_Anti=MarkovCls.continuous_to_discrete(TRANS_MATRIX_COMBO,DELTA_T)


# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    1.00,   # Well
    0.20,   # Stroke
    0.90,    # Post-Stroke
    0,     # stroke Dead
    0      # Non-stroke Dead
    ]

# annual cost of each health  states
ANNUAL_STATE_COST = [
    0,   # Well
    5000,    # Stroke
    200,    # Post-Stroke
    0,         # stroke Dead
    0        # Non-stroke Dead
    ]

ANNUAL_STATE_COST_ANTI = [
    0,   # Well
    5000,    # Stroke
    750,    # Post-Stroke
    0,         # stroke Dead
    0        # Non-stroke Dead
    ]

# annual state costs
Stroke_COST = 5000
Poststroke_COST = 200

#treatment cost
Treat_COST = 2000

class give_marrix():
    def __init__(self):
        self._matrixwithouttheraoy = TRANS_MATRIX
        self._matrixwiththeraoy = TRANS_MATRIX_COMBO
        self._PROBmatrixwiththeraoy = Prob_TransMatrix_Anti
        self._PROBmatrixwithouttheraoy = Prob_TransMatrix_None


    def get_non_matrix(self):
        return self._matrixwithouttheraoy

    def get_non_prob(self):
        return self._PROBmatrixwithouttheraoy

    def get_with_matrix(self):
        return self._matrixwiththeraoy

    def get_with_prob(self):
        return self._PROBmatrixwiththeraoy

