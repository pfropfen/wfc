# WAVE FUNCTION TILE LOOKUP TABLE

tileCompatibilityList = [0b001001111, # gras
                         0b000000011, # wald
                         0b000000001, # kuh
                         0b000011001, # strand
                         0b000111000, # wasser
                         0b000010000, # fisch
                         0b011000011, # berg
                         0b111000000, #bergschnee
                         0b010000000] #schneemann
                   

tileCompatibilityLookUpTable = {0b000000001:0b001001111, # gras
                                0b000000010:0b000000011, # wald
                                0b000000100:0b000000001, # kuh
                                0b000001000:0b000011001, # strand
                                0b000010000:0b000111000, # wasser
                                0b000100000:0b000010000, # fisch
                                0b001000000:0b011000011, # berg
                                0b010000000:0b111000000, #bergschnee
                                0b100000000:0b010000000} #schneemann
                                
binaryLookUpTable = {"grass":0b000000001,
                     "wald":0b000000010,
                     "kuh":0b000000100,
                     "strand":0b000001000,
                     "wasser":0b000010000,
                     "fisch":0b000100000,
                     "berg":0b001000000,
                     "bergschnee":0b010000000,
                     "schneemann":0b100000000}