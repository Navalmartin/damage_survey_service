MIR_HOST_URL: str = "http://0.0.0.0:8001" 
MIR_API_URL: str = f"{MIR_HOST_URL}/api"
MIR_API_VERSION: str = 'v1'

DEFAULT_ABNORMAL_EVENTS_MSG: str = "No abnormal events reporeted."
INVALID_EMAIL_STR = 'test@email.com'

SI_ITEMS = {'BILGE_PUMPS': ['Bilge Pumps', [{'chpt_id': 1, 'checkpoint_type': 'MANUAL_BILGE_PUMP', 'description': 'Manual bilge pump(s)'}, {'chpt_id': 2, 'checkpoint_type': 'ELECTRIC_AUTOMATIC_BILGE_PUMPS', 'description': 'Electric/automatic bilge pump(s)'}, {'chpt_id': 3, 'checkpoint_type': 'BILGE_ALARMS', 'description': 'Bilge alarms'}]], 'RIG_AND_SAILS': ['Rig and Sails', [{'chpt_id': 1, 'checkpoint_type': 'MAST_MAST_BEND', 'description': 'Mast & mast bend'}, {'chpt_id': 2, 'checkpoint_type': 'MAST_FOOT_THROUGH_DECK', 'description': 'Mast foot/through-deck'}, {'chpt_id': 3, 'checkpoint_type': 'SHROUDS_PS_SWAGE', 'description': 'Shrouds PS swage'}, {'chpt_id': 4, 'checkpoint_type': 'SHROUDS_PS_TURNBUCKLE', 'description': 'Shrouds PS turnbuckle & pins'}, {'chpt_id': 5, 'checkpoint_type': 'SHROUDS_SB_SWAGE', 'description': 'Shrouds SB swage'}, {'chpt_id': 6, 'checkpoint_type': 'SHROUDS_SB_TURNBUCKLE', 'description': 'Shrouds SB turnbuckle & pins'}, {'chpt_id': 7, 'checkpoint_type': 'FORESTAY_INNER_STAY', 'description': 'Forestay & pins'}, {'chpt_id': 8, 'checkpoint_type': 'INNER_STAYS', 'description': 'Inner stay(s)'}, {'chpt_id': 9, 'checkpoint_type': 'BACKSTAY', 'description': 'Backstay'}, {'chpt_id': 10, 'checkpoint_type': 'BACKSTAY_TENSIONER', 'description': 'Backstay tensioner'}, {'chpt_id': 11, 'checkpoint_type': 'RUNNERS', 'description': 'Runners'}, {'chpt_id': 12, 'checkpoint_type': 'GOOSENECK', 'description': 'Gooseneck(s)'}, {'chpt_id': 13, 'checkpoint_type': 'BOOM', 'description': 'Boom'}, {'chpt_id': 14, 'checkpoint_type': 'SPINNAKER_POLE', 'description': 'Spinnaker pole'}, {'chpt_id': 15, 'checkpoint_type': 'JOCKEY_POLE', 'description': 'Jockey pole'}, {'chpt_id': 16, 'checkpoint_type': 'FURLING_GEAR', 'description': 'Furling gear'}, {'chpt_id': 17, 'checkpoint_type': 'MAIN_SHEET_CONTROL', 'description': 'Main sheet control'}, {'chpt_id': 18, 'checkpoint_type': 'RUNNING_RIGGING', 'description': 'Running rigging'}, {'chpt_id': 19, 'checkpoint_type': 'SAILS', 'description': 'Sails'}, {'chpt_id': 20, 'checkpoint_type': 'MASTHEAD_SENSOR', 'description': 'Masthead sensor'}]], 'STEERING': ['Steering', [{'chpt_id': 1, 'checkpoint_type': 'RUDDER_FOUNDATIONS', 'description': 'Rudder foundations'}, {'chpt_id': 2, 'checkpoint_type': 'BEARINGS', 'description': 'Bearings or pintles and gudgeons'}, {'chpt_id': 3, 'checkpoint_type': 'GLANDS', 'description': 'Rudder glands'}, {'chpt_id': 4, 'checkpoint_type': 'CABLES', 'description': 'Cables'}, {'chpt_id': 5, 'checkpoint_type': 'CHAINS', 'description': 'Chains'}, {'chpt_id': 6, 'checkpoint_type': 'GEAR', 'description': 'Gear'}, {'chpt_id': 7, 'checkpoint_type': 'HOSES', 'description': 'Hoses'}, {'chpt_id': 8, 'checkpoint_type': 'HELM_TILLER', 'description': 'Helm/tiller'}, {'chpt_id': 9, 'checkpoint_type': 'EMERGENCY_TILLER_STEERING_SYSTEM', 'description': 'Emergency tiller/steering system'}]], 'DOMESTIC_EQUIPMENT': ['Domestic Equipment', [{'chpt_id': 1, 'checkpoint_type': 'PROPANE_LOCKER_SHUT_OFF_VALVE', 'description': 'Propane locker/shut off valve'}, {'chpt_id': 2, 'checkpoint_type': 'PROPANE_COOKER_HOSE', 'description': 'Propane cooker/hose'}, {'chpt_id': 3, 'checkpoint_type': 'GAS_LOCKER_GRAVITY_VENT', 'description': 'Gas locker gravity vent'}, {'chpt_id': 4, 'checkpoint_type': 'GAS_ALARM', 'description': 'Gas alarm'}, {'chpt_id': 5, 'checkpoint_type': 'GRAY_BLACK_WATER_TANK', 'description': 'Gray/black water tanks'}, {'chpt_id': 6, 'checkpoint_type': 'HEADS', 'description': 'Heads'}, {'chpt_id': 7, 'checkpoint_type': 'VENTILATION', 'description': 'Ventilation'}, {'chpt_id': 8, 'checkpoint_type': 'HVAC', 'description': 'Heating Ventilation AirCon'}, {'chpt_id': 9, 'checkpoint_type': 'REFRIGERATION', 'description': 'Refrigeration'}, {'chpt_id': 10, 'checkpoint_type': 'WASTE_HANDLING', 'description': 'Waste handling'}, {'chpt_id': 11, 'checkpoint_type': 'FRESH_WATER_MAKER_FILTRATION', 'description': 'Fresh water maker/filtration'}]], 'CATHODIC_PROTECTION': ['Cathodic Protection', [{'chpt_id': 1, 'checkpoint_type': 'ANODES', 'description': 'Anodes'}, {'chpt_id': 2, 'checkpoint_type': 'GROUNDING_CIRCUIT', 'description': 'Grounding circuit'}, {'chpt_id': 3, 'checkpoint_type': 'GROUNDING_STRAP', 'description': 'Grounding straps'}, {'chpt_id': 4, 'checkpoint_type': 'BI_METALLIC_CONNECTION', 'description': 'Bi-metallic connection (mast, cable trays, pipes, etc.)'}, {'chpt_id': 5, 'checkpoint_type': 'STERN_TUBE_GLANDS', 'description': 'Stern tube glands'}, {'chpt_id': 6, 'checkpoint_type': 'PROPELLER_SHAFT_COUPLING', 'description': 'Propeller shaft coupling'}, {'chpt_id': 7, 'checkpoint_type': 'GROUNDING_OF_MASTS', 'description': 'Grounding of masts'}, {'chpt_id': 8, 'checkpoint_type': 'INSULATION_BETWEEN_DISSIMILAR_METALS_AND_THE_HULL_DECK', 'description': ' Insulation between dissimilar metals & the hull/deck'}]], 'KEELS_BALLAST': ['Keels Ballast', [{'chpt_id': 1, 'checkpoint_type': 'BALLAST_KEEL_HULL_JOINT_EXTERNAL', 'description': 'Ballast keel/hull joint (external)'}, {'chpt_id': 2, 'checkpoint_type': 'KEEL_UNDERSIDE_EXTERNAL', 'description': 'Keel underside (external)'}, {'chpt_id': 3, 'checkpoint_type': 'KEEL_BOLTS_INTERNAL', 'description': 'Keel bolts (internal)'}, {'chpt_id': 4, 'checkpoint_type': 'KEEL_MATRIX_GRID_KEELSON', 'description': 'Keel matrix (grid or keelson)'}, {'chpt_id': 5, 'checkpoint_type': 'CENTRELINE_JOINT_EXTERNAL', 'description': 'Centreline joint external'}, {'chpt_id': 6, 'checkpoint_type': 'DEMIHULL_AND_FIN_KEELS', 'description': 'Demihull & fin keels'}]], 'SAFETY_EQUIPMENT': ['Safety Equipment', [{'chpt_id': 1, 'checkpoint_type': 'LIFE_RAFTS_AND_RELEASE', 'description': 'Life raft(s) & release (capacity & validity)'}, {'chpt_id': 2, 'checkpoint_type': 'LIFEBUOYS', 'description': 'Lifebuoy(s) (numbers & validity)'}, {'chpt_id': 3, 'checkpoint_type': 'MOB', 'description': 'MOB (numbers & validity)'}, {'chpt_id': 4, 'checkpoint_type': 'LIFEJACKETS_AND_HARNESS', 'description': 'Lifejackets(s) & harnesses (numbers & validity)'}, {'chpt_id': 5, 'checkpoint_type': 'THERMAL_PROTECTIVE_AIDS', 'description': 'Thermal protective aids (numbers & validity)'}, {'chpt_id': 6, 'checkpoint_type': 'VHF', 'description': 'VHF (DCS/Range)/Portable VHF '}, {'chpt_id': 7, 'checkpoint_type': 'EPIRB', 'description': 'EPIRB (validity)'}, {'chpt_id': 8, 'checkpoint_type': 'SART', 'description': 'SART (validity)'}, {'chpt_id': 9, 'checkpoint_type': 'PYROTECHNICS', 'description': 'Pyrotechnics (numbers and validity)'}, {'chpt_id': 10, 'checkpoint_type': 'FIRE_EXTINGUISHERS', 'description': 'Fire extinguishers (numbers and validity)'}, {'chpt_id': 11, 'checkpoint_type': 'SIGNAGE', 'description': 'Signage'}, {'chpt_id': 12, 'checkpoint_type': 'FOG_HORN', 'description': 'Fog horn'}, {'chpt_id': 13, 'checkpoint_type': 'SEARCH_LIGHTS', 'description': 'Search lights'}, {'chpt_id': 14, 'checkpoint_type': 'SAFETY_MANUAL_BOOKLET', 'description': 'Safety manual/booklet'}, {'chpt_id': 15, 'checkpoint_type': 'REMOVABLE_JACKLINES', 'description': 'Removable jacklines'}, {'chpt_id': 16, 'checkpoint_type': 'LANYARD_AND_KILL_SWITCH', 'description': 'Lanyard and kill switch'}]], 'DECK_EQUIPMENT': ['Deck Equipment', [{'chpt_id': 1, 'checkpoint_type': 'STANCHIONS', 'description': 'Stanchions'}, {'chpt_id': 2, 'checkpoint_type': 'HATCHES_PORTS', 'description': 'Hatches/ports'}, {'chpt_id': 3, 'checkpoint_type': 'VENTS_THROUGH_DECK_FITTINGS', 'description': 'Vents/through-deck fittings'}, {'chpt_id': 4, 'checkpoint_type': 'WINCHES_BOLLARDS_CLEATS', 'description': 'Winches, bollards, cleats'}, {'chpt_id': 5, 'checkpoint_type': 'CHAINPLATES', 'description': 'Chainplates'}, {'chpt_id': 6, 'checkpoint_type': 'CHAINPLATE_THROUGH_DECK', 'description': 'Chainplate through-deck'}, {'chpt_id': 7, 'checkpoint_type': 'WINDLASS_GROUND_GEAR', 'description': 'Windlass/ground gear'}, {'chpt_id': 8, 'checkpoint_type': 'ANCHOR_ROLLER_CHAIN_STOPPER', 'description': 'Anchor, roller and chain stopper'}, {'chpt_id': 9, 'checkpoint_type': 'CHAIN_LOCKER_DRAIN', 'description': 'Chain locker/drain'}, {'chpt_id': 10, 'checkpoint_type': 'PASSERELLE', 'description': 'Passerelle'}, {'chpt_id': 11, 'checkpoint_type': 'TENDER_DAVITS_ARCH', 'description': 'Tender davits/arch'}, {'chpt_id': 12, 'checkpoint_type': 'MOORING_LINES', 'description': 'Mooring lines'}, {'chpt_id': 13, 'checkpoint_type': 'FENDERS', 'description': 'Fenders'}, {'chpt_id': 14, 'checkpoint_type': 'TANK_DECK_FILLERS', 'description': 'Tank deck fillers'}, {'chpt_id': 15, 'checkpoint_type': 'BIMINI_DODGER', 'description': 'Bimini/Dodger'}, {'chpt_id': 16, 'checkpoint_type': 'BOAT_COVERS', 'description': 'Boat cover'}, {'chpt_id': 17, 'checkpoint_type': 'TOWING_POST_BRIDLE', 'description': 'Towing post/bridle'}, {'chpt_id': 18, 'checkpoint_type': 'FOREDECK', 'description': 'Foredeck'}, {'chpt_id': 19, 'checkpoint_type': 'NON_SKID_SURFACING', 'description': 'Non skid surfacing'}, {'chpt_id': 20, 'checkpoint_type': 'DECK_AFT', 'description': 'Deck aft'}, {'chpt_id': 21, 'checkpoint_type': 'SUPERSTRUCTURES', 'description': 'Superstructure'}, {'chpt_id': 22, 'checkpoint_type': 'COCKPITS', 'description': 'Cockpit(s)'}, {'chpt_id': 23, 'checkpoint_type': 'DECK_HULL_JOINTS_INTERNAL_EXTERNAL', 'description': 'Deck/hull joints internal external'}, {'chpt_id': 24, 'checkpoint_type': 'EMERGENCY_ESCAPE_HATCH', 'description': 'Emergency escape hatch'}]], 'HULL_SHELL': ['Hull Shell', [{'chpt_id': 1, 'checkpoint_type': 'HIN', 'description': 'Hull identification number'}, {'chpt_id': 2, 'checkpoint_type': 'TRANSOM_NAME', 'description': 'Vessel name & port'}, {'chpt_id': 3, 'checkpoint_type': 'HULL_FWD_SB', 'description': 'Hull forward SB'}, {'chpt_id': 4, 'checkpoint_type': 'HULL_FWD_PS', 'description': 'Hull forward PS'}, {'chpt_id': 5, 'checkpoint_type': 'HULL_MIDSHIP_SB', 'description': 'Hull midship SB'}, {'chpt_id': 6, 'checkpoint_type': 'HULL_MIDSHIP_PS', 'description': 'Hull midship PS'}, {'chpt_id': 7, 'checkpoint_type': 'HULL_AFT_SB', 'description': 'Hull aft SB'}, {'chpt_id': 8, 'checkpoint_type': 'HULL_AFT_PS', 'description': 'Hull aft PS'}, {'chpt_id': 9, 'checkpoint_type': 'TRANSOM_HATCH_GARAGE', 'description': 'Transom (hatch/garage)'}, {'chpt_id': 10, 'checkpoint_type': 'KEELSON_BILGE_KEELS', 'description': 'Keelson/bilge keels'}, {'chpt_id': 11, 'checkpoint_type': 'HULL_BRIDGE_DECK', 'description': 'Hull-bridge deck'}, {'chpt_id': 12, 'checkpoint_type': 'HULL_INBOARD_FORWARD_SB', 'description': 'Hull inboard forward SB'}, {'chpt_id': 13, 'checkpoint_type': 'HULL_INBOARD_FORWARD_PS', 'description': 'Hull inboard forward PS'}, {'chpt_id': 14, 'checkpoint_type': 'HULL_INBOARD_MIDSHIP_SB', 'description': 'Hull inboard midship SB'}, {'chpt_id': 15, 'checkpoint_type': 'HULL_INBOARD_MIDSHIP_PS', 'description': 'Hull inboard midship PS'}, {'chpt_id': 16, 'checkpoint_type': 'HULL_INBOARD_AFT_SB', 'description': 'Hull inboard aft SB'}, {'chpt_id': 17, 'checkpoint_type': 'HULL_INBOARD_AFT_PS', 'description': 'Hull inboard aft PS'}, {'chpt_id': 18, 'checkpoint_type': 'TRANSOMS_JOINTS', 'description': 'Transoms & joints'}, {'chpt_id': 19, 'checkpoint_type': 'TUBE_SEAMS', 'description': 'Tube seams'}, {'chpt_id': 20, 'checkpoint_type': 'TUBE_HULL_SEAMS', 'description': 'Tube/hull seams'}, {'chpt_id': 21, 'checkpoint_type': 'HATCHES_PORTS_BELOW_DECK_EDGE', 'description': 'Tube/hull seams'}, {'chpt_id': 22, 'checkpoint_type': 'TRANSOM_MOUNT_FOR_OUTBOARD_ENGINES', 'description': 'Transom mount for outboard engines'}, {'chpt_id': 23, 'checkpoint_type': 'DRAIN_POINTS_ON_DECK_AND_HATCHES', 'description': 'Drain points on deck & hatches'}]], 'INTERNAL_STRUCTURE_MEMBERS': ['Internal Structure Members', [{'chpt_id': 1, 'checkpoint_type': 'MAST_HEEL_MATRIX', 'description': 'Mast heel/matrix'}, {'chpt_id': 2, 'checkpoint_type': 'BULKHEADS', 'description': 'Bulkheads'}, {'chpt_id': 3, 'checkpoint_type': 'FRAMES', 'description': 'Frames'}, {'chpt_id': 4, 'checkpoint_type': 'STRINGERS', 'description': 'Stringers'}, {'chpt_id': 5, 'checkpoint_type': 'CARLINGS', 'description': 'Carlings'}, {'chpt_id': 6, 'checkpoint_type': 'DECK_HULL_JOINTS_INTERNAL', 'description': 'Deck/hull joints internal'}, {'chpt_id': 7, 'checkpoint_type': 'DECK_HULL_JOINTS_EXTERNAL', 'description': 'Deck/hull joints external'}, {'chpt_id': 8, 'checkpoint_type': 'CHAIN_PLATE_FOUNDATIONS', 'description': 'Chain plate foundations'}, {'chpt_id': 9, 'checkpoint_type': 'LIMBER_HOLES', 'description': 'Limber holes'}, {'chpt_id': 10, 'checkpoint_type': 'CROSS_BEAM_BRIDGE_DECK_TO_HULL', 'description': 'Cross beam/Bridge deck to hull'}, {'chpt_id': 11, 'checkpoint_type': 'STRINGERS_ADJACENT_TO_WAVE_SLAMMING_ZONE', 'description': 'Stringers adjacent to wave slamming zone'}, {'chpt_id': 12, 'checkpoint_type': 'HULL_TRANSOM_JOINT', 'description': 'Hull/transom joint'}]], 'ELECTRICAL_AND_ELECTRONICS': ['Electrical and Electronics', [{'chpt_id': 1, 'checkpoint_type': 'BATTERY_STOWAGE_TRAY_STRAPS_VENTILATION', 'description': 'Battery stowage/tray/straps/ventilation'}, {'chpt_id': 2, 'checkpoint_type': 'BATTERY_HARNESS', 'description': 'Batteries harness'}, {'chpt_id': 3, 'checkpoint_type': 'BATTERY_ISOLATORS_CHARGING_SWITCH_DIODES', 'description': 'Battery isolators/charging switch or diodes'}, {'chpt_id': 4, 'checkpoint_type': 'INVERTER_CHARGE_CONTROLLER', 'description': 'Inverter/charge controller'}, {'chpt_id': 5, 'checkpoint_type': 'DOMESTIC_LIGHTING', 'description': 'Domestic lighting'}, {'chpt_id': 6, 'checkpoint_type': 'NAVIGATION_LIGHTS_ANCHOR_LIGHT', 'description': 'Navigation lights/anchor light'}, {'chpt_id': 7, 'checkpoint_type': 'DC_CABLES', 'description': 'DC cables'}, {'chpt_id': 8, 'checkpoint_type': 'AC_CABLES_CABINET_EARTHING', 'description': 'AC cables/Cabinet earthing'}, {'chpt_id': 9, 'checkpoint_type': 'BREAKER', 'description': 'Breakers'}, {'chpt_id': 10, 'checkpoint_type': 'NAVIGATION_EQUIPMENT', 'description': 'Navigation equipment & instruments'}, {'chpt_id': 11, 'checkpoint_type': 'AUTOPILOT', 'description': 'Autopilot'}, {'chpt_id': 12, 'checkpoint_type': 'AIS_TRANSPONDER', 'description': 'AIS transponder'}, {'chpt_id': 13, 'checkpoint_type': 'RADAR', 'description': 'Radar'}, {'chpt_id': 14, 'checkpoint_type': 'SATCOM', 'description': 'Satellite array'}]], 'INTERIOR_EXTERIOR_OUTFIT': ['Interior Exterior Outfit', [{'chpt_id': 1, 'checkpoint_type': 'JOINERY', 'description': 'Joinery'}, {'chpt_id': 2, 'checkpoint_type': 'HEAD_LININGS', 'description': 'Head linings'}, {'chpt_id': 3, 'checkpoint_type': 'SALOON', 'description': 'Saloon'}, {'chpt_id': 4, 'checkpoint_type': 'GALLEY', 'description': 'Galley'}, {'chpt_id': 5, 'checkpoint_type': 'MASTER_CABIN', 'description': 'Master cabin'}, {'chpt_id': 6, 'checkpoint_type': 'GUEST_CABIN', 'description': 'Guest cabin(s)'}, {'chpt_id': 7, 'checkpoint_type': 'CREW_CABIN', 'description': 'Crew cabin(s)'}, {'chpt_id': 8, 'checkpoint_type': 'HEADS', 'description': 'Heads'}, {'chpt_id': 9, 'checkpoint_type': 'TECHNICAL_ROOM', 'description': 'Technical room'}, {'chpt_id': 10, 'checkpoint_type': 'SOFT_FURNISHING_EXTERIOR', 'description': 'Soft furnishing (exterior)'}, {'chpt_id': 11, 'checkpoint_type': 'FLOORBOARDS', 'description': 'Floorboards/carpets'}, {'chpt_id': 12, 'checkpoint_type': 'BRIGHTWORKS_EXTERNAL', 'description': 'Brightworks (external)'}, {'chpt_id': 13, 'checkpoint_type': 'TEAK_DECKS_SEAMS_PLUGS', 'description': 'Teak decks, seams & plugs'}]], 'PROPULSION_MACHINERY': ['Propulsion Machinery', [{'chpt_id': 1, 'checkpoint_type': 'ENGINE_LOCKER_ROOM', 'description': 'Engine locker/room'}, {'chpt_id': 2, 'checkpoint_type': 'ENGINE', 'description': 'Engine(s)'}, {'chpt_id': 3, 'checkpoint_type': 'ENGINE_BUILDER_PLAQUE', 'description': "Engine builder's plaque with engine number"}, {'chpt_id': 4, 'checkpoint_type': 'HOSE_CLAMPS ', 'description': 'Hoses & hose clamps'}, {'chpt_id': 5, 'checkpoint_type': 'LUBRICATION_COOLANT', 'description': 'Lubrication/coolant'}, {'chpt_id': 6, 'checkpoint_type': 'FUEL_FILTER', 'description': 'Fuel filters/shut-off valve'}, {'chpt_id': 7, 'checkpoint_type': 'STERN_TUBE', 'description': 'Stern tube(s) and/or saildrive(s)'}, {'chpt_id': 8, 'checkpoint_type': 'PROPELLER_EXTERNAL', 'description': 'Propeller(s)'}, {'chpt_id': 9, 'checkpoint_type': 'SHAFT_BEARING', 'description': 'Shaft bearing(s)'}, {'chpt_id': 10, 'checkpoint_type': 'MORSE_CONTROL', 'description': 'Morse control(s)'}, {'chpt_id': 11, 'checkpoint_type': 'OILY_SUMP', 'description': 'Oily sump/bilges'}, {'chpt_id': 12, 'checkpoint_type': 'GENERATOR', 'description': 'Generator(s)'}, {'chpt_id': 13, 'checkpoint_type': 'ALTERNATOR', 'description': 'Alternator/belt'}, {'chpt_id': 14, 'checkpoint_type': 'WET_EXHAUST_LINE', 'description': 'Wet exhaust line (date)'}, {'chpt_id': 15, 'checkpoint_type': 'BOW_THRUSTER', 'description': 'Bow thruster/stern thruster'}, {'chpt_id': 16, 'checkpoint_type': 'HYDRAULIC_PACK', 'description': 'Hydraulic pack & lines'}]], 'THROUGH_HULL_FITTINGS': ['Through Hull Fittings', [{'chpt_id': 1, 'checkpoint_type': 'ENGINE_EXHAUST', 'description': 'Engine exhaust'}, {'chpt_id': 2, 'checkpoint_type': 'ENGINE_INTAKE', 'description': 'Raw water intake(s) & filter'}, {'chpt_id': 3, 'checkpoint_type': 'SENSOR', 'description': 'Sensors (depth, speed)'}, {'chpt_id': 4, 'checkpoint_type': 'HEADS_INTAKE', 'description': 'Heads intake & siphon break'}, {'chpt_id': 5, 'checkpoint_type': 'HEADS_OUTLET', 'description': 'Heads outlet & vent'}, {'chpt_id': 6, 'checkpoint_type': 'AC_REFRIGERATION', 'description': 'AC/refrigeration'}, {'chpt_id': 7, 'checkpoint_type': 'KEEL_COOLING', 'description': 'Keel cooling'}, {'chpt_id': 8, 'checkpoint_type': 'UNDERWATER_LIGHTING', 'description': 'Underwater lighting'}, {'chpt_id': 9, 'checkpoint_type': 'SEACOCK', 'description': 'Seacocks (material and grounding)'}]]}