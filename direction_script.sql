CREATE OR REPLACE FUNCTION directions(line1 geometry, line2 geometry)
  RETURNS INTEGER AS $$
  DECLARE angle1 FLOAT := ST_AZIMUTH (ST_STARTPOINT(line1), ST_ENDPOINT(line1))*180/pi();
  DECLARE angle2 FLOAT := ST_AZIMUTH (ST_STARTPOINT(line2), ST_ENDPOINT(line2))*180/pi();

BEGIN
  IF (ABS(angle2 - angle1) < 15) OR ABS(angle2 - angle1) < 195 AND ABS(angle2-angle1)>165 OR (angle2-angle1>345) AND (angle2-angle1<360) THEN RETURN 0; --Straight
    ElSIF (angle2-angle1 > 15 ) AND (angle2-angle1 < 85) THEN RETURN 1; --Sharp left
    ELSIF (angle2-angle1 >85) AND (angle2-angle1 <95) THEN RETURN 2; --Left turn
    ELSIF (angle2-angle1 >95) AND (angle2-angle1 < 165) THEN RETURN 3; --Slight left
    ELSIF (angle2-angle1 >195) AND (angle2-angle1 < 265) THEN RETURN 4; --Slight right
    ELSIF (angle2-angle1 >265) AND (angle2-angle1 < 275) THEN RETURN 5; --Right turn
    ELSIF (angle2-angle1 >275) AND (angle2-angle1 <345) THEN RETURN 6; --Sharp Right
    ELSE RETURN -1;
  END IF;
END;
$$ LANGUAGE plpgsql;