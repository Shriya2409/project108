import random
import plotly_express as px
import plotly.figure_factory as ff

counter=[]
sum=[]

for i in range(1,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    sum.append(dice1+ dice2)
    counter.append(i)

fig=px.bar(x=sum, y=counter)
#fig.show()

fig2=ff.create_distplot([sum], ["result"])
fig2.show()