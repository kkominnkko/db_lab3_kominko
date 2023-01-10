DO $$
 DECLARE
     hname	  heroescopy.hero_name%TYPE;
     category     heroescopy.category_id%TYPE;
     roles   heroescopy.role_id%TYPE;
     strength heroescopy.hero_strength%TYPE;
	 agility heroescopy.hero_agility%TYPE;
	 intelligence heroescopy.hero_intelligence%TYPE;

 BEGIN
 	 hname := 'Mirana';
	 category := 3;
     roles := 2;
     strength := 18;
	 agility := 18;
	 intelligence := 22;
     FOR counter IN 1..10
         LOOP
            INSERT INTO heroescopy (hero_name, category_id, role_id, hero_strength, hero_agility, hero_intelligence)
             VALUES (hname || counter + 1, category + counter,  counter + 1, counter + 1, counter + 1, counter + 1);
         END LOOP;
 END;
 $$
 
 