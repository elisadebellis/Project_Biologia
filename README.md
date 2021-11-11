# Project_Biologia

Input:
  - Cartella degli esperimenti

Output 
  - Cartella dei risultati 


------------------------------------------------------------------------------
0. La funzione explore_dir(dir):
 
 - prende in input la Cartella contenente gli esperimenti
 - crea una nuova cartella "Results" in cui verranno inseriti i file con i risultati finali 
 - crea un file denominato con il nome dell'esperimento

1. Inizializzazione del dizionario

2. La funzione analisi_dati(dir):

  - prende in input una directory contente i file.csv 
  - fa un controllo con la funzione check(dir) se la directory inserita e' corretta
  - legge il primo file.csv e inizia a scrivere sul dizionario nel seguente modo:

      chiave: ID 
      valore: lista dei corrispondenti valori associati all'id
    
      dizionario = {ID:[region_name, region_area, area_unit, object_count, object_area, slice_counting]}
      
      se le informazioni region_area, object_count, object_area, slice_counting sono gia' presenti per quell'ID, esse vengono aggiunte alle precedenti.
   - vengono aggiunti i nomi dei file che hanno contribuito alle informazioni precedenti

3. La funzione write_on_file(dict,dir,workbook):
   
   -prende in input un dizionario, una directory, e un workbook
   -aggiunge un nuovo sheet al file
   -scrive sulla prima riga le intestazioni delle varie colonne in esame
   -popola le caselle del file.xsls con le informazioni salvate sul dizionario
    quindi per ogni ID aggiunge su ogni colonna i corrispondenti valori
   

    

  
