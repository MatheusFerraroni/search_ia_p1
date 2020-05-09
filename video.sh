clear
sleep 2
start=`date +%s`

echo "  _______                  _               _   _                 __ "
echo " |__   __|                | |             | | | |               /_ |"
echo "    | |     ____    ____  | |__     ____  | | | |__     ___      | |"
echo "    | |    |  __|  / _  | |  _ \   / _  | | | |  _ \   / _ \     | |"
echo "    | |    | |    | (_| | | |_) | | (_| | | | | | | | | (_) |    | |"
echo "    |_|    |_|     \__,_| |_.__/   \__,_| |_| |_| |_|  \___/     |_|"
echo ""
echo ""
echo "Aissa Hadj - 265189"
echo "Lucas Zanco Ladeira - 188951"
echo "Matheus Ferraroni - 212142"
echo "Maria Vitória Rodrigues Oliveira - 262884"
echo "Oscar Ciceri - 164786"
sleep 5



show_maps()
{
  mapa=$1
  cat $mapa
  sleep 1
}

for i in 1 2 3 4 5 6 7 8 9 10 11 12
do
  clear
  echo "Show all maps: $i/12"
  show_maps "./maps2/no_points/map$i.txt"
  clear
  echo "Show all maps: $i/12"
  show_maps "./maps2/with_points/map$i.txt"
done
clear


run_mapa()
{
  mapa=$1
  method=$2
  echo "Map:      $mapa"
  echo "Command: python main.py --$method --maps=$mapa"
  cat $mapa
  echo ""
  python main.py --$method --maps=$mapa
  sleep 2
}


for m in bfs dfs hill best ucs aos ats lbs
do
  for i in 1 
  do
    clear
    echo "Strategy $m/[bfs dfs hill best ucs aos ats lbs]"
    run_mapa "./maps2/with_points/map$i.txt" $m
  done
done

end=`date +%s`
runtime=$((end-start))
echo $runtime