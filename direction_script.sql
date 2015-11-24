CREATE OR REPLACE FUNCTION directions(geometry, geometry ) RETURNS INTEGER as $$
BEGIN
  DECLARE angle1 float;
  DECLARE angle2 float;
  SET angle1 = ST_AZIMUTH(ST_STARTPOINT($1), ST_ENDPOINT($1))*180/pi();
  SET angle2 = ST_AZIMUTH(ST_STARTPOINT($2), ST_ENDPOINT($2))*180/pi();

  if ABS(angle1-angle2) < 15 THEN SELECT 1;
  ELSE IF 