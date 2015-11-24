CREATE OR REPLACE FUNCTION directions(line1 geometry, line2 geometry)
  RETURNS INTEGER AS $$
  DECLARE angle1 FLOAT := ST_AZIMUTH (ST_STARTPOINT(line1), ST_ENDPOINT(line1))*180/pi();
  DECLARE angle2 FLOAT := ST_AZIMUTH (ST_STARTPOINT(line2), ST_ENDPOINT(line2))*180/pi();

BEGIN
  IF (ABS(angle1 - angle2) < 15) THEN RETURN 0; --Straight
  ELSIF (angle1-angle2 > 45) AND (angle1-angle2 < 75) THEN RETURN 1; --Slight Left
  ELSIF (angle1-angle2 >= 75) AND (angle1-angle2 < 100) THEN RETURN 2;  --Left
  ELSIF (angle1-angle2 >=100) THEN RETURN 3;  --Sharp left
  ELSIF (angle2 - angle1 > 45) AND (angle2-angle1 < 75) THEN RETURN 4; --Slight right
  ELSIF (angle2 - angle1 >= 75) AND (angle2-angle1 < 100) THEN RETURN 5; --Right
  ELSIF (angle2 - angle1 >= 100) THEN RETURN 6; --Sharp Right
  ELSE RETURN -1;
  END IF;
END;
$$ LANGUAGE plpgsql;