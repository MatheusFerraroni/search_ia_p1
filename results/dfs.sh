for ((n=1;n<10;n++))
do
	echo $n
	python ../main.py --dfs --map="../maps/map$n.txt" | grep -e Time -e Node | sed 's/^......//' > dfs_map$n.out
	for ((i=0;i<32;i++))
	do
		python ../main.py --dfs --map="../maps/map$n.txt" | grep -e Time -e Node | sed 's/^......//' >> dfs_map$n.out
	done 
	python compute.py --file="./dfs_map$n.out"
done
