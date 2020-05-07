# for value in lbs dfs bfs aos ats 
# do

#   echo ${value}

#   for ((n=1;n<16;n++))
#   do
#   	echo $value " MAP1-Scenario = " $n

#   	python main.py --$value --print --map="./maps/map$n.txt" | grep -e Time -e Node -e Pont -e Left -e Acti -e Nods -e Expa -e Exps | sed 's/^......//' > ./results/maps1/${value}_map$n.out
#   	for ((i=0;i<10;i++))
#   	do
#   		echo "Seed = " $i
#   		python main.py --$value --print --map="./maps/map$n.txt" | grep -e Time -e Node -e Pont -e Left -e Acti -e Nods -e Expa -e Exps | sed 's/^......//' >> ./results/maps1/${value}_map$n.out
#   	done
#   	python ./results/compute.py --file="./results/maps1/${value}_map$n.out"

#   done

# done

########################################## WITH POINTS ########################################################

for value in hill dfs bfs aos ats lbs 
do

 echo ${value}

 for ((n=1;n<13;n++))
 do
   echo $value " MAP2-Scenario = " $n

   python main.py --$value --print --map="./maps2/with_points/map$n.txt" | grep -e Time -e Node  -e Pont -e Left -e Acti -e Expa | sed 's/^......//' > ./results/with_points/${value}_map$n.out
   for ((i=0;i<10;i++))
   do
     echo "Seed = " $i
     python main.py --$value --print --map="./maps2/with_points/map$n.txt" | grep -e Time -e Node   -e Pont -e Left -e Acti -e Expa | sed 's/^......//' >> ./results/with_points/${value}_map$n.out
   done
   python ./results/compute.py --file="./results/with_points/${value}_map$n.out"

 done

done

########################################## NO POINTS ########################################################

# for value in lbs dfs bfs aos ats 
# do

#   echo ${value}

#   for ((n=1;n<13;n++))
#   do
#     echo $value " MAP3-Scenario = " $n

#     python main.py --$value --print --map="./maps2/no_points/map$n.txt" | grep -e Time -e Node  -e Pont -e Left -e Acti | sed 's/^......//' > ./results/no_points/${value}_map$n.out
#     for ((i=0;i<10;i++))
#     do
#       echo "Seed = " $i
#       python main.py --$value --print --map="./maps2/no_points/map$n.txt" | grep -e Time -e Node   -e Pont -e Left -e Acti | sed 's/^......//' >> ./results/no_points/${value}_map$n.out
#     done
#     python ./results/compute.py --file="./results/no_points/${value}_map$n.out"

#   done

# done