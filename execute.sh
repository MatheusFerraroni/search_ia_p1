for value in bfs dfs lbs hill best
do

  echo ${value}

  for ((n=1;n<16;n++))
  do
  	echo $n

  	python3 main.py --$value --print --map="./maps/map$n.txt" | grep -e Time -e Node | sed 's/^......//' > ./results/${value}_map$n.out
  	for ((i=0;i<32;i++))
  	do
  		python3 main.py --$value --print --map="./maps/map$n.txt" | grep -e Time -e Node | sed 's/^......//' >> ./results/${value}_map$n.out
  	done
  	python3 ./results/compute.py --file="./results/${value}_map$n.out"

  done

done
