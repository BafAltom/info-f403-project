info-f403-project
=================

Compiler of a simplified version of Perl into Android ASM.

# Instructions (in french)

Pour lancer le programme, tapez la commande :

	python compilateur.py -v -i  <fichier perl>

L'option -v est optionnelle, si sélectionnée, le programme affichera dans le terminal le résultat de chaque étape intermédiaire.
Le code sera créé dans un fichier de même nom que celui du fichier d'input.

Nous avons également inclus des fichiers perl testant notre projet (ainsi que les fichiers assembleurs correspondant générés par notre compilateur), dans le dossier inputTests. Pour de plus ample détails, voir les commentaires de ces fichiers.

Il est également possible de lancer chaque partie séparément, elle afficheront alors dans le terminal le résultat.
Cela se fait au moyen de ces commandes :

	python scanner.py -i <fichier perl>
	python parser.py -i <fichier perl>
	python syntaxtreeabstracter.py -i <fichier perl>
	python codeGeneration.py -i <fichier perl>

Le code assembleur ainsi produit a été conçu et testé pour être compilé avec le compilateur android-ndk-r8d et testé avec adb, via ces commandes (une fois l'émulateur lancé, ou un smartphone android connecté).

	android-ndk-r8d/toolchains/arm-linux-androideabi-4.7/prebuilt/linux-x86/bin/arm-linux-androideabi-as -o program.o program.S
	android-ndk-r8d/toolchains/arm-linux-androideabi-4.7/prebuilt/linux-x86/bin/arm-linux-androideabi-ld -s -o exécutable program.o
	adb push exécutable /data/local/tmp/
	adb shell /data/local/tmp/exécutable

Il suffit de modifier la partie <linux-x86> en fonction du système d'exploitation.

Nous avons également développé quelques outils au cours du projet qui, s'ils ne sont pas nécessaire pour notre compilateur, nous semblaient néanmoins intéressants. Nous les avons donc laissé :
* `python printFirstFollowActionTable.py` Affiche les first, follow et action table de notre grammaire
* `python cfgrammar_tests.py` Vérifie que les grammaires stockées dans cfgrammar (grammaire du projet et des TP) sont LL(1)
* `python parser_test.py` Affiche le parseTree du fichier <test5.pl> qui est présenté dans l'annexe du rapport (Fig 17)
