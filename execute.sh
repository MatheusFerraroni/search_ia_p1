for value in lbs dfs bfs aos ats 
do

  echo ${value}

  for ((n=1;n<16;n++))
  do
  	echo $value " MAP1-Scenario = " $n

  	python main.py --$value --print --map="./maps/map$n.txt" | grep -e Time -e Node  -e Pont -e Left -e Acti | sed 's/^......//' > ./results/${value}_map$n.out
  	for ((i=0;i<5;i++))
  	do
  		echo "Seed = " $i
  		python main.py --$value --print --map="./maps/map$n.txt" | grep -e Time -e Node   -e Pont -e Left -e Acti | sed 's/^......//' >> ./results/${value}_map$n.out
  	done
  	python ./results/compute.py --file="./results/${value}_map$n.out"

  done

done

# for value in lbs dfs bfs aos ats 
# do

#   echo ${value}

#   for ((n=1;n<12;n++))
#   do
#     echo $value " MAP2-Scenario = " $n

#     python main.py --$value --print --map="./maps2/with_points/map$n.txt" | grep -e Time -e Node  -e Pont -e Left -e Acti | sed 's/^......//' > ./results_with_points/${value}_map$n.out
#     for ((i=0;i<2;i++))
#     do
#       echo "Seed = " $i
#       python main.py --$value --print --map="./maps/with_points/map$n.txt" | grep -e Time -e Node   -e Pont -e Left -e Acti | sed 's/^......//' >> ./results_with_points/${value}_map$n.out
#     done
#     python ./results/compute.py --file="./results_with_points/${value}_map$n.out"

#   done

# done

# for value in lbs dfs bfs aos ats 
# do

#   echo ${value}

#   for ((n=1;n<12;n++))
#   do
#     echo $value " MAP3-Scenario = " $n

#     python main.py --$value --print --map="./maps2/no_points/map$n.txt" | grep -e Time -e Node  -e Pont -e Left -e Acti | sed 's/^......//' > ./results/results_no_points/${value}_map$n.out
#     for ((i=0;i<2;i++))
#     do
#       echo "Seed = " $i
#       python main.py --$value --print --map="./maps/no_points/map$n.txt" | grep -e Time -e Node   -e Pont -e Left -e Acti | sed 's/^......//' >> ./results/results_no_points/${value}_map$n.out
#     done
#     python ./results/compute.py --file="./results_no_points/${value}_map$n.out"

#   done

# done