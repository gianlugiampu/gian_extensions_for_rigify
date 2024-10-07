# Rig Extensions for Rigify
-------

This provides a set of experimental custom metarigs and a new rig types.

There are no previous version of the extensions, but to use the latest version:
use `Code > Download ZIP` to obtain a ZIP archive of the code, and install it
as a Feature Set through the Rigify Add-On settings.

## Custom Metarigs
-------

* ### Eyebrows Metarig
  Generate a metarig with 7 bones for Eyebrows UI, and a `basic.raw_copy` as UI master control.
  * `brow_inner.L/R` `brow_middle.L/R` `brow_outer.L/R` `brow_master`

* ### Eyes Metarig
  Generate a metarig with 6 bones for Eyes UI, and a `basic.raw_copy` as UI master control.
  * `eye_aim.L/R` `eyelid.L/R` `eyeopen.L/R`
 
* ### Nose & Cheeks Metarig
  Generate a metarig with 4 bones for Nose and Cheeks UI, and a `basic.raw_copy` as UI master control.
  * `nose_sneer.L/R` `cheek_squint.L/R`
 
* ### Mouth & Jaw Metarig
  Generate a metarig with 22 bones for Mouth UI, 2 bones for Jaw UI and 1 bone for Tongue UI, and a `basic.raw_copy` as UI master control.
  * `mouth_press.L/R` `mouth_dimple.L/R` `mouth_smile.L/R` `mouth_stretch.L/R` `mouth_frown.L/R` `mouth_upper.L/R` `mouth_lower.L/R` `lip_upper` `lip_lower` `mouth_pucker` `mouth_close` `mouth_funnel` `mouth`
  * `jaw_target` `jaw_forward` `tongue_out`
 
* ### Face Metarig
  Generate a metarig all the previous metarig sets, and a `basic.raw_copy` as UI master control.
  * `Eyebrows metarig` `Eyes metarig` `Nose & Cheeks metarig` `Mouth & Jaw metarig` 
  

## Rig Types
-------

* ### UI Slider ('gian.ui.slider')

  Generate a container bone with name 'PAN_boneName' and a control bone 'boneName',
  with a limit location constraint based on lenght of bone.
  
  #### Custom Options
  * **slider_type** specifies the type of slider between Small (rectangle) and Large (square);
  * **minimal_design** generate a minimal style designed PAN control;
  * **clamp_up_down** Cut the Pan area and set control limit from 0 to positive bone lenght (Clamp Up) or from 0 to negative bone lenght (Clamp Down);
  * **custom_title** Generate a custom text resposive with the PAN designs. With `@name` tag the text will have the bone name (Text font is Ubuntu Medium.);
  * **fill_slider** Check to fill the shape of the slider control widget; 
  * **Relink Constraint** Replace the parent with a different bone after all bones are created. Using simply CTRL, DEF or MCH will replace the prefix instead;
  * **Assign Slider Collection** Assign slider control to different Bone Collections;
 
* ### UI Custom Text ('gian.ui.custom_text')

  Generate a simple bone with custom text widget. Text font is Ubuntu Medium.
  
  #### Custom Options
  * **custom_text** Generate a custom text resposive with bone size;

## Contributing
If you'd like to contribute to the development of the Rig Extensions, you are always welcome! If you want to contribute to this list, send a _pull request_, open an _issue_ or _contact with me.

## Credits
-------
Thanks to Adriano D'Elia for procedural widget generation nodes.

> Adriano D'Elia [Link](https://linktr.ee/adrianodelia)

#### Authored and maintained by Gianluca Giampuzzo
