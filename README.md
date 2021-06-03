# BattleDev S17

Ma participation à la BattleDev saison 17. Seuls les 4 premiers exercices (sur 6) ont été résolus.

J'étais sur le 5^e^, mais je suis resté sur une approche naïve ne permettant pas de trouver la saolution dans le temps imparti, il faudrait utiliser les techniques de [programmation dynamique](https://fr.wikipedia.org/wiki/Programmation_dynamique) pour en tirer une solution satisfaisante.

Classé 171^e^ / 3190 participants

## Script

`test.sh` permet d'effectuer des tests en local en téléchargeant le jeu de donné dans le dossier approprié (*ici les jeux de données des exercices 3, 4 et 5 sont présents, les deux premiers étant très simples*)

La syntaxe est la suivante : `./test.sh <exo> <nb tests>`

*Exemple :*

```
$ ./test.sh 3 3
   ========== Test n°1/3 ==========
..........
#..##..###
......#.#.
##...##.##
...###.##.
....#.#..#
##.#######
##.#######
##.#######
##.#######
..##..##..
###.#.##.#
.##....##.
#.##..#..#
##.##..#.#
..##..#.##
.###..####
..##....#.
...#.##...
.#.##.###.
real 0.02
user 0.01
sys 0.00
OK

   ========== Test n°2/3 ==========
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
#.#...####
####...#..
..##.##.#.
####.#..#.
.###...#..
#....#.###
.##...#.##
real 0.02
user 0.02
sys 0.00
OK

   ========== Test n°3/3 ==========
..#..#...#
.#...#.#.#
####...#..
#.#..#.#.#
.#.#.#..#.
######.###
######.###
######.###
######.###
..#.#.#...
####...##.
.##.####..
.###.#....
.#..###...
....#...#.
######.###
######.###
######.###
######.###
.#.##.##.#
real 0.01
user 0.01
sys 0.00
OK

Success !
```

