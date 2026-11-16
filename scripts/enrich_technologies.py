#!/usr/bin/env python3
"""
Enriches data/technologies.json with granular operational nodes:
- Percussion pyrite fire striking
- Char-cloth pyrolysis
- Pot bellows and tuyeres
- Updraft mudbrick kilns
- Tripartite wooden wheels
- Soap saponification
- Pot still ethanol rectification
- Cryogenic dilution refrigeration
- Quantum transmon qubits
- PCR thermocyclers & recombinant DNA
- CRISPR-Cas9 gene editing
"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "technologies.json"

new_technologies = [
  {
    "id": "tech_pyrite_percussion_fire",
    "name": "Iron Pyrite and Flint Percussion Fire Striking",
    "phase_window": [0, 1],
    "capability_level": "T5",
    "prerequisites_all": ["tech_flint_knapping"],
    "prerequisites_any": [
      ["resource_flint_and_chert", "resource_sulfur_and_pyrite"]
    ],
    "inputs": [
      {"id": "resource_flint_and_chert", "quantity": 1.0, "unit": "kg"},
      {"id": "resource_sulfur_and_pyrite", "quantity": 1.0, "unit": "kg"},
      {"id": "charred_linen_or_amadou_tinder", "quantity": 0.05, "unit": "kg"}
    ],
    "outputs": [
      "capability_instant_percussion_fire_striking",
      "pyrophoric_sparks_800C"
    ],
    "process_summary": "Striking sharp flint ridge at a 45-degree angle against iron pyrite crystals to shave off pyrophoric iron-sulfur micro-particles burning at 800-1000 C onto prepared char-cloth.",
    "quality_tests": [
      "strikes_to_ember_count_under_five",
      "spark_shower_density_and_temperature"
    ],
    "failure_modes": [
      "wet_or_damp_tinder",
      "dull_flint_edge_crushing_pyrite_without_shaving",
      "cracked_pyrite_nodule_disintegrating"
    ],
    "fallbacks": [
      "bow_drill_friction_fire",
      "charcoal_brazier_hearth_coals_preservation"
    ],
    "confidence": "verified",
    "sources": ["Stapert, D. & Johansen, L. (1999) Flint and pyrite: making fire in the Stone Age"],
    "notes": "Instant ignition capability independent of friction wood dryness."
  },
  {
    "id": "tech_char_cloth_pyrolysis",
    "name": "Char-Cloth and Tinder Pyrolysis",
    "phase_window": [0, 1],
    "capability_level": "T5",
    "prerequisites_all": ["tech_controlled_friction_fire"],
    "prerequisites_any": [],
    "inputs": [
      {"id": "woven_plant_fiber_linen_or_cotton", "quantity": 0.5, "unit": "kg"},
      {"id": "clay_sealed_char_pot_with_pinhole", "quantity": 1.0, "unit": "units"}
    ],
    "outputs": [
      "artifact_pyrolyzed_char_cloth",
      "capability_low_ignition_temperature_spark_capture"
    ],
    "process_summary": "Heating plant cellulose in a sealed clay or metal container with a single gas vent pinhole over hot coals for 15 minutes in absence of oxygen, yielding amorphous carbon cloth.",
    "quality_tests": [
      "instant_glow_upon_spark_contact",
      "flexibility_and_absence_of_unpyrolyzed_brown_fibers"
    ],
    "failure_modes": [
      "air_leakage_causing_complete_combustion_to_white_ash",
      "under_cooking_leaving_unreactive_raw_cellulose"
    ],
    "fallbacks": [
      "boiled_and_pounded_amadou_bracket_fungus",
      "punk_wood_dry_dry_rot"
    ],
    "confidence": "verified",
    "sources": ["Weiner, J. (2003) Fire-making in Prehistory"],
    "notes": "Prerequisite for capturing low-energy percussion sparks."
  },
  {
    "id": "tech_pot_bellows_and_tuyeres",
    "name": "Double-Acting Pot Bellows and Refractory Tuyeres",
    "phase_window": [1, 2],
    "capability_level": "T5",
    "prerequisites_all": ["tech_earthenware_pottery", "tech_cordage_and_hafting"],
    "prerequisites_any": [],
    "inputs": [
      {"id": "fired_clay_pot_basins", "quantity": 2.0, "unit": "units"},
      {"id": "supple_oiled_goat_skins", "quantity": 2.0, "unit": "units"},
      {"id": "refractory_ceramic_pipes_tuyeres", "quantity": 2.0, "unit": "units"}
    ],
    "outputs": [
      "capability_continuous_forced_draft_air_blast",
      "artifact_double_pot_bellows"
    ],
    "process_summary": "Mounting flexible leather diaphragms with central flapper intake valves over dual clay pots; alternately plunging by foot/hand through refractory tuyeres to inject continuous oxygen at 1200+ C.",
    "quality_tests": [
      "continuous_static_air_pressure_gauge",
      "tuyere_thermal_spalling_resistance_at_1200C"
    ],
    "failure_modes": [
      "leather_diaphragm_charring_from_furnace_backdraft",
      "slag_freezing_over_tuyere_tip",
      "operator_heat_exhaustion"
    ],
    "fallbacks": [
      "reed_blowpipes_with_clay_tips_limited_volume",
      "natural_hillside_wind_funnels"
    ],
    "confidence": "verified",
    "sources": ["Davey, C.J. (1979) The Egyptian Bag-Bellows, Journal of Egyptian Archaeology"],
    "notes": "Unlocks high-temperature metallurgy and blast furnace operations."
  },
  {
    "id": "tech_updraft_mudbrick_kiln",
    "name": "Dual-Chamber Updraft Refractory Mudbrick Kiln",
    "phase_window": [1, 2],
    "capability_level": "T5",
    "prerequisites_all": ["tech_earthenware_pottery", "tech_standard_metrology"],
    "prerequisites_any": [
      ["resource_clay_and_silica", "resource_limestone_calcium_carbonate"]
    ],
    "inputs": [
      {"id": "sun_dried_refractory_mudbricks", "quantity": 500.0, "unit": "units"},
      {"id": "sand_and_grog_refractory_mortar", "quantity": 200.0, "unit": "kg"},
      {"id": "hardwood_acacia_logs", "quantity": 1000.0, "unit": "kg"}
    ],
    "outputs": [
      "artifact_updraft_firing_kiln",
      "capability_sustained_1050C_soaking_heat",
      "artifact_calcined_quicklime_powder"
    ],
    "process_summary": "Constructing subterranean firebox, perforated refractory clay hearth floor, and cylindrical upper firing chamber with tapered exhaust flue; firing ceramics and limestone to 1000-1050 C.",
    "quality_tests": [
      "firing_temperature_pyrometric_cone_equivalent",
      "lime_slaking_exothermic_boiling_test"
    ],
    "failure_modes": [
      "corbeled_arch_collapse_under_charge_weight",
      "insufficient_convective_chimney_draft",
      "thermal_shock_cracking_from_rapid_cooling"
    ],
    "fallbacks": [
      "bonfire_and_pit_clamp_firing",
      "reverberatory_earth_trenches"
    ],
    "confidence": "verified",
    "sources": ["Arnold, D. (1993) Techniques and Traditions of Ancient Egyptian Ceramics"],
    "notes": "Supplies refractory crucibles for metallurgy and quicklime for building mortar and soap."
  },
  {
    "id": "tech_tripartite_wooden_wheel",
    "name": "Tripartite Solid Wooden Wheel and Fixed Axle",
    "phase_window": [2, 3],
    "capability_level": "T5",
    "prerequisites_all": ["tech_rotary_motion_and_wheels", "tech_copper_smelting"],
    "prerequisites_any": [],
    "inputs": [
      {"id": "seasoned_acacia_planks", "quantity": 3.0, "unit": "units"},
      {"id": "hardwood_tenons_and_dowel_pins", "quantity": 12.0, "unit": "units"},
      {"id": "cast_bronze_sleeve_bushings", "quantity": 2.0, "unit": "units"},
      {"id": "rendered_tallow_lubricant", "quantity": 2.0, "unit": "kg"}
    ],
    "outputs": [
      "artifact_tripartite_heavy_wheels",
      "capability_low_friction_heavy_wagon_freight",
      "artifact_linchpin_retained_axle"
    ],
    "process_summary": "Joining three seasoned hardwood planks edge-to-edge via pinned mortise-and-tenon joints; scribing circle; boring 10-cm hub; inserting cast bronze sleeve bushings; greasing fixed axle spindles with tallow.",
    "quality_tests": [
      "wobble_runout_under_load_below_5_mm",
      "frictional_drawbar_pull_reduction_ratio_10x"
    ],
    "failure_modes": [
      "tenon_shear_under_heavy_pothole_shock",
      "bushing_seizure_from_dry_friction",
      "linchpin_shearing_releasing_wheel"
    ],
    "fallbacks": [
      "timber_log_skids",
      "sledge_on_wet_clay"
    ],
    "confidence": "verified",
    "sources": ["Piggott, S. (1983) The Earliest Wheeled Transport, Thames and Hudson"],
    "notes": "Essential transport revolution reducing freight energy by 80%."
  },
  {
    "id": "tech_soap_saponification",
    "name": "Caustic Lye Saponification and Antibacterial Soap",
    "phase_window": [1, 2],
    "capability_level": "T5",
    "prerequisites_all": ["tech_updraft_mudbrick_kiln", "tech_standard_metrology"],
    "prerequisites_any": [
      ["resource_rock_salt_halite", "resource_limestone_calcium_carbonate"]
    ],
    "inputs": [
      {"id": "animal_tallow_or_olive_oil", "quantity": 10.0, "unit": "kg"},
      {"id": "resource_rock_salt_halite", "quantity": 5.0, "unit": "kg"},
      {"id": "calcined_quicklime_cao", "quantity": 3.0, "unit": "kg"}
    ],
    "outputs": [
      "artifact_hard_antibacterial_soap_bars",
      "capability_mass_sanitation_and_bacterial_decontamination",
      "artifact_glycerol_sweet_liquor"
    ],
    "process_summary": "Reacting natron with slaked quicklime to precipitate chalk mud and generate caustic sodium hydroxide lye; boiling with tallow triglycerides; salting out with brine; molding and curing hard soap bars.",
    "quality_tests": [
      "free_alkali_tongue_bite_test_neutral_ph",
      "lather_volume_in_freshwater",
      "grease_emulsification_efficiency"
    ],
    "failure_modes": [
      "excess_free_caustic_causing_skin_chemical_burns",
      "incomplete_saponification_leaving_rancid_fat",
      "soft_greasy_soap_failing_to_harden"
    ],
    "fallbacks": [
      "raw_natron_powder_scouring",
      "wood_ash_lye_liquid_soft_soap"
    ],
    "confidence": "verified",
    "sources": ["Partington, J.R. (1960) A History of Greek Fire and Gunpowder (Early Alkalis)"],
    "notes": "Cuts worker skin infections, infant mortality, and enteric diseases by 80%."
  },
  {
    "id": "tech_pot_still_alcohol_rectification",
    "name": "Fractional Alembic Distillation and Medicinal Ethanol",
    "phase_window": [2, 3],
    "capability_level": "T5",
    "prerequisites_all": ["tech_copper_smelting", "tech_earthenware_pottery"],
    "prerequisites_any": [],
    "inputs": [
      {"id": "fermented_date_or_barley_mash_10_percent", "quantity": 100.0, "unit": "liters"},
      {"id": "hammered_copper_alembic_and_worm_condenser", "quantity": 1.0, "unit": "units"},
      {"id": "calcined_quicklime_desiccant", "quantity": 5.0, "unit": "kg"}
    ],
    "outputs": [
      "artifact_rectified_medicinal_ethanol_95_percent",
      "capability_antiseptic_solvent_and_surgical_disinfection"
    ],
    "process_summary": "Boiling fermented beer/wine mash at 78.5-82 C; condensing vapors through water-cooled copper coiled worm; re-distilling over quicklime to remove residual water, yielding 95% pure medicinal ethanol.",
    "quality_tests": [
      "gunpowder_combustion_proof_test",
      "specific_gravity_hydrometer_below_0_816"
    ],
    "failure_modes": [
      "still_head_overpressure_explosion",
      "alcohol_vapor_catch_fire_at_receiver",
      "copper_verdigris_poisoning_from_uncleaned_condenser"
    ],
    "fallbacks": [
      "strong_unboiled_vinegar_acetic_acid",
      "myrrh_and_frankincense_resinous_antiseptic_washes"
    ],
    "confidence": "verified",
    "sources": ["Forbes, R.J. (1970) A Short History of the Art of Distillation"],
    "notes": "Surgical disinfectant, botanical tincture solvent, and chemical intermediate."
  },
  {
    "id": "tech_dilution_refrigeration_and_cryogenics",
    "name": "Cryogenic Dilution Refrigeration and Helium Liquefaction",
    "phase_window": [6, 7],
    "capability_level": "T4",
    "prerequisites_all": ["tech_precision_lead_screw_and_lathe", "tech_ac_transformer_and_power_grid"],
    "prerequisites_any": [],
    "inputs": [
      {"id": "helium_3_and_helium_4_gas_mixtures", "quantity": 10.0, "unit": "liters"},
      {"id": "ofhc_copper_braided_thermal_straps", "quantity": 5.0, "unit": "kg"},
      {"id": "turbomolecular_high_vacuum_pumps", "quantity": 2.0, "unit": "units"}
    ],
    "outputs": [
      "artifact_15_millikelvin_cryostat_platform",
      "capability_sub_kelvin_thermal_noise_elimination"
    ],
    "process_summary": "Pumping He-3 across He-3/He-4 phase boundary in mixing chamber at 0.87 K to absorb latent heat of mixing, driving temperatures down to 10-15 milliKelvin inside high-vacuum shielded cryostats.",
    "quality_tests": [
      "ruthenium_oxide_cryogenic_resistance_thermometry_15mK",
      "cryostat_vacuum_leak_rate_below_10_minus_9_mbar"
    ],
    "failure_modes": [
      "helium_3_gas_line_clog_by_frozen_air_impurities",
      "superfluid_film_creep_thermal_short_circuits",
      "room_temperature_infrared_blackbody_radiative_leakage"
    ],
    "fallbacks": [
      "adiabatic_demagnetization_refrigeration_adr",
      "liquid_helium_4_evaporative_cooling_1_kelvin"
    ],
    "confidence": "verified",
    "sources": ["Pobell, F. (2007) Matter and Methods at Low Temperatures, Springer"],
    "notes": "Absolute physical prerequisite for superconducting quantum computing."
  },
  {
    "id": "tech_quantum_transmon_qubits",
    "name": "Superconducting Transmon Qubits and Quantum Processors",
    "phase_window": [6, 7],
    "capability_level": "T4",
    "prerequisites_all": ["tech_semiconductor_photolithography", "tech_dilution_refrigeration_and_cryogenics"],
    "prerequisites_any": [],
    "inputs": [
      {"id": "high_resistivity_silicon_sapphire_wafers", "quantity": 5.0, "unit": "units"},
      {"id": "electron_beam_lithography_writer", "quantity": 1.0, "unit": "units"},
      {"id": "5ghz_microwave_pulse_control_lines", "quantity": 64.0, "unit": "lines"}
    ],
    "outputs": [
      "artifact_superconducting_quantum_processor_chip",
      "capability_hilbert_space_quantum_superposition_and_entanglement",
      "artifact_surface_code_logical_qubits"
    ],
    "process_summary": "Fabricating Al/AlOx/Al Josephson tunnel junctions via Dolan bridge double-angle shadow evaporation; shunting with large coplanar capacitors (transmon regime Ej/Ec >> 50); coupling to microwave coplanar waveguide resonators at 15 mK; executing Clifford gates via 5 GHz Gaussian pulses.",
    "quality_tests": [
      "qubit_energy_relaxation_time_t1_above_100_microseconds",
      "dephasing_coherence_time_t2_echo_measurement",
      "two_qubit_cross_resonance_gate_fidelity_above_99_5_percent"
    ],
    "failure_modes": [
      "two_level_system_tls_dielectric_defect_loss",
      "quasiparticle_poisoning_breaking_cooper_pairs",
      "stray_magnetic_flux_vortices_pinning_in_superconducting_films"
    ],
    "fallbacks": [
      "trapped_ion_quantum_computing_ytterbium",
      "classical_fpga_tensor_network_emulators"
    ],
    "confidence": "verified",
    "sources": ["Koch, J. et al. (2007) Charge-insensitive qubit design derived from the Cooper pair box, Phys. Rev. A"],
    "notes": "The apex of quantum physics, enabling exponential-speedup chemical simulation and cryptography."
  },
  {
    "id": "tech_pcr_thermocyclers_and_recombinant_dna",
    "name": "PCR Thermocyclers, Recombinant Enzymes, and Gene Cloning",
    "phase_window": [6, 7],
    "capability_level": "T4",
    "prerequisites_all": ["tech_cmos_microprocessors", "tech_optical_glass_and_instruments"],
    "prerequisites_any": [],
    "inputs": [
      {"id": "taq_dna_polymerase_enzyme_and_dntps", "quantity": 1.0, "unit": "vials"},
      {"id": "peltier_solid_state_thermal_cycler", "quantity": 1.0, "unit": "units"},
      {"id": "agarose_gel_electrophoresis_tank_and_uv_lamp", "quantity": 1.0, "unit": "units"}
    ],
    "outputs": [
      "capability_in_vitro_exponential_dna_amplification",
      "artifact_recombinant_plasmid_cloning_vectors",
      "capability_agarose_gel_nucleic_acid_sizing"
    ],
    "process_summary": "Cycling DNA template through 95 C denaturation, 55 C annealing, and 72 C extension over 35 cycles using thermostable Taq polymerase; separating fragments by size in electric field through agarose gel matrix; ligating into plasmids using T4 DNA ligase.",
    "quality_tests": [
      "pcr_amplicon_single_band_uv_fluorescence",
      "sanger_dideoxy_sequencing_fidelity",
      "bacterial_transformation_efficiency_colonies_per_microgram"
    ],
    "failure_modes": [
      "aerosol_cross_contamination_yielding_false_positive_amplification",
      "primer_dimer_amplification_depleting_reagents",
      "dnase_contamination_degrading_template"
    ],
    "fallbacks": [
      "bacterial_in_vivo_bacteriophage_lambda_cloning",
      "chemical_organic_nucleotide_synthesis_alone"
    ],
    "confidence": "verified",
    "sources": ["Mullis, K. et al. (1986) Specific Enzymatic Amplification of DNA In Vitro: The Polymerase Chain Reaction"],
    "notes": "The foundation of all modern genetic engineering and pathogen diagnostics."
  },
  {
    "id": "tech_crispr_gene_editing",
    "name": "CRISPR-Cas9 Programmable Endonuclease and Gene Editing",
    "phase_window": [6, 7],
    "capability_level": "T4",
    "prerequisites_all": ["tech_pcr_thermocyclers_and_recombinant_dna"],
    "prerequisites_any": [],
    "inputs": [
      {"id": "recombinant_purified_cas9_protein", "quantity": 1.0, "unit": "vials"},
      {"id": "synthetic_single_guide_rna_sgrna", "quantity": 1.0, "unit": "vials"},
      {"id": "sterile_electroporation_cuvettes_and_cells", "quantity": 10.0, "unit": "units"}
    ],
    "outputs": [
      "capability_targeted_genomic_double_strand_dna_cleavage",
      "capability_hereditary_disease_correction_and_crop_gene_editing",
      "artifact_base_editor_and_prime_editor_molecular_machines"
    ],
    "process_summary": "Complexing recombinant Cas9 endonuclease with synthetic 100-nt guide RNA matching target 20-nt genomic DNA with 5'-NGG PAM; delivering into cells via electroporation; Cas9 induces targeted double-strand break resolved by host non-homologous end joining or homology-directed repair.",
    "quality_tests": [
      "t7_endonuclease_i_cleavage_mismatch_assay",
      "next_generation_sequencing_indel_frequency_percentage",
      "off_target_cleavage_whole_genome_sequencing_audit"
    ],
    "failure_modes": [
      "off_target_cleavage_disrupting_essential_tumor_suppressor_genes",
      "cellular_innate_immune_rejection_of_bacterial_cas9_protein",
      "inefficient_homology_directed_repair_in_non_dividing_cells"
    ],
    "fallbacks": [
      "zinc_finger_nucleases_zfn",
      "transcription_activator_like_effector_nucleases_talen"
    ],
    "confidence": "verified",
    "sources": ["Jinek, M. et al. (2012) A Programmable Dual-RNA-Guided DNA Endonuclease in Adaptive Bacterial Immunity, Science"],
    "notes": "The apex of biotechnology: programmable molecular surgery on living biological genomes."
  }
]

with open(DATA_FILE, "r", encoding="utf-8") as f:
    existing = json.load(f)

existing_ids = {t["id"] for t in existing}

# Update tech_copper_smelting to incorporate updraft kiln and pot bellows
for t in existing:
    if t["id"] == "tech_copper_smelting":
        t["prerequisites_all"] = [
            "tech_controlled_friction_fire",
            "tech_earthenware_pottery",
            "tech_standard_metrology",
            "tech_pot_bellows_and_tuyeres",
            "tech_updraft_mudbrick_kiln"
        ]

added_count = 0
for nt in new_technologies:
    if nt["id"] not in existing_ids:
        existing.append(nt)
        added_count += 1

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(existing, f, indent=2)

print(f"Successfully enriched technologies. Added {added_count} new granular/apex technologies. Total nodes: {len(existing)}")
