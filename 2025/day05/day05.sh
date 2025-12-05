INPUT=input.txt

# put counter in a file because a while loop part of pipeline starts a subshell
# and won't have access to a global counter variable.
fresh_ingredients_counter=$(mktemp)
echo 0 > $fresh_ingredients_counter

grep -oE '^[0-9]+$' $INPUT | while read ingredient; do

    grep '-' $INPUT | while IFS='-' read start end; do
      #echo $start $end
      if (( $start <= $ingredient && $ingredient <= $end )); then
#          echo "Fresh: $start <= $ingredient <= $end"
          current_count=$(<"$fresh_ingredients_counter")
          new_count=$(( current_count + 1 ))
          echo $new_count > "$fresh_ingredients_counter"
          break
      fi
    done
    #echo Spoiled: $ingredient

done


cat $fresh_ingredients_counter
rm -f $fresh_ingredients_counter
