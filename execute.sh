for value in dfs bfs aos ats lbs
do

  echo ${value}

  for ((n=1;n<16;n++))
  do
  	echo "Scenario = " $n

  	python main.py --$value --print --map="./maps/map$n.txt" | grep -e Time -e Node  -e Pont -e Left | sed 's/^......//' > ./results/${value}_map$n.out
  	for ((i=0;i<32;i++))
  	do
  		echo "Seed = " $i
  		python main.py --$value --print --map="./maps/map$n.txt" | grep -e Time -e Node   -e Pont -e Left | sed 's/^......//' >> ./results/${value}_map$n.out
  	done
  	python ./results/compute.py --file="./results/${value}_map$n.out"

  done

done

