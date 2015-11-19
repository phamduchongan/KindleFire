#KindleFire
+#This code block will calculate the evasion of the hero (dota 2)
+print "Please enter the number of evasion item"
+number_of_evasion = int(raw_input("> "))
+t = 1 
+chance_getting_hit = 1 
+while t <= number_of_evasion:
+        t = t+1 
+        global chance_getting_hit
+        print "Please enter the ratio of evasion "
+        evasion_item = float(raw_input("> "))
+        chance_getting_hit = (1-evasion_item) * chance_getting_hit
+        
+        
+print "The chance of you getting hit: ",chance_getting_hit*100
