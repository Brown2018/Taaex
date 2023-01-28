
from django import forms
from GestionCouriers.models import *
from django.forms import ModelForm

SEXE_CHOICES = [
    ('M', 'M'),
    ('F', 'F'),
]

FORM_JURIDIQUE_CHOICES = [
('L\’entreprise individuelle (ou établissement)','L\’entreprise individuelle (ou établissement) '),
('La Société à Responsabilité Limitée (S.A.R.L)','La Société à Responsabilité Limitée (S.A.R.L)'),
('La Société Anonyme (S.A)','La Société Anonyme (S.A)'),
('La Société par Actions Simplifiées (S.A.S.)','La Société par Actions Simplifiées (S.A.S.)'),
('La Société en Nom Collectif (S.N.C)','La Société en Nom Collectif (S.N.C)'),
('La Société en Commandite Simple (S.C.S)','La Société en Commandite Simple (S.C.S)'),
('Le Groupement d\’Intérêt Economique (G.I.E)','Le Groupement d\’Intérêt Economique (G.I.E)')
]

