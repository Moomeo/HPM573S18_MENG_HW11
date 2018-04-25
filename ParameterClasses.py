from enum import Enum
import InputData as Data


class HealthStats(Enum):
    """ health states of patients with HIV """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    DEATH = 3
    Non_stroke_death = 4


class Therapies(Enum):
    """ mono vs. combination therapy """
    NONE = 0
    ANTICOAG = 1


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        # calculate the adjusted discount rate
        self._adjDiscountRate = Data.DISCOUNT * Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL

        # annual treatment cost
        if self._therapy == Therapies.NONE:
            self._annualTreatmentCost = 0
        else:
            self._annualTreatmentCost = 0

        # transition probability matrix of the selected therapy
        self._prob_matrix = []

        # calculate transition probabilities depending of which therapy options is in use
        if therapy == Therapies.NONE:
            self._prob_matrix = Data.Prob_TransMatrix_None[0]
        else:
            self._prob_matrix = Data.Prob_TransMatrix_Anti[0]

        # calculate  annual state costs depending of which therapy options is in use
        if therapy == Therapies.NONE:
            self._annualStateCosts = Data.ANNUAL_STATE_COST
        else:
            self._annualStateCosts = Data.ANNUAL_STATE_COST_ANTI

        # annual state  utilities
        self._annualStateUtilities = Data.ANNUAL_STATE_UTILITY

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_adj_discount_rate(self):
        return self._adjDiscountRate

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

    def get_annual_state_cost(self, state):
        return self._annualStateCosts[state.value]

    def get_annual_state_utility(self, state):
        return self._annualStateUtilities[state.value]

    def get_annual_treatment_cost(self):
        return self._annualTreatmentCost
