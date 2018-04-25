import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import InputData as Data

m=Data.give_marrix()

# QUESTION 1
print("Trans Matrix without therapy:",m.get_non_matrix())
print("Probability Matrix without therapy:",m.get_non_prob())

# QUESTION 2
print("Trans Matrix with therapy:",m.get_with_matrix())
print("Probability Matrix without therapy:",m.get_with_prob())

# QUESTION 3
# create and simulate cohort with treatment
cohort1 = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)

simOutputs1 = cohort1.simulate()
#print out discounted total cost and discounted total utility
SupportMarkov.print_outcomes(simOutputs1, 'Anticoagulation:')

# create and simulate cohort with out treatment
cohort2 = MarkovCls.Cohort(
    id=2,
    therapy=P.Therapies.NONE)

simOutputs2 = cohort2.simulate()


# QUESTION 1
print("Trans Matrix without therapy:")

# QUESTION 4
#  cost-utility plane and net monetary benefit curve
SupportMarkov.report_CEA_CBA(simOutputs2,simOutputs1)


