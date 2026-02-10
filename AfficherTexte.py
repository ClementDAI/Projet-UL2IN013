import pygame 

pygame.init()

Bleu_saphir=(1,49,180)

petite_police= pygame.font.Font("mytype.ttf",24)

commande_c=petite_police.render("Commande C en cours d'utilisation", True, Bleu_saphir)
commande_a=petite_police.render("Commande A en cours d'utilisation", True, Bleu_saphir)
texte_controleC=petite_police.render("touche C : Faire un carré", True, Bleu_saphir)
texte_controleA=petite_police.render("touche A : Aller vers des coordonnées à entrer", True, Bleu_saphir)

def afficher_le_texte(surface_cible, touche_pressee):
    if touche_pressee=="menu" or touche_pressee is None:
        surface_cible.blit(texte_controleA, (10, 0))
        surface_cible.blit(texte_controleC, (10, 20))
    if touche_pressee == "a":
        surface_cible.blit(commande_a, (10, 0))
    elif touche_pressee == "c":
        surface_cible.blit(commande_c, (10, 0))
    
