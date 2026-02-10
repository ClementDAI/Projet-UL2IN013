import pygame 

pygame.init()

Bleu_saphir=(1,49,180)

petite_police= pygame.font.Font("mytype.ttf",24)

commande_c=petite_police.render("Vous utilisez la commande c", True, Bleu_saphir)
commande_a=petite_police.render("Vous utilisez la commande a", True, Bleu_saphir)
texte_menu=petite_police.render("Vous devez choisir: C: Tracer carre | A: aller ", True, Bleu_saphir)

def afficher_le_texte(surface_cible, touche_pressee):
    if touche_pressee=="menu" or touche_pressee is None:
        surface_cible.blit(texte_menu, (20, 80))
    if touche_pressee == "a":
        surface_cible.blit(commande_a, (20, 80))
    elif touche_pressee == "c":
        surface_cible.blit(commande_c, (20, 80))
    
