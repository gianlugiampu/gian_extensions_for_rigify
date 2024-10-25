import bpy
from mathutils import Color, Vector

def create(obj):
    """
    Creates a metarig sample for a Eyebrows Ui rig.

    Args:
        obj: The object to create the metarig for.

    Returns:
        A list of bones in the metarig.
    
    PS: Generated by rigify.utils.write_metarig
    """
    
    #Get Armature Data
    arm = obj.data
    
    #Setup Color Sets
    arm.rigify_colors_lock = False
    
    #Dict with color params normal, select and active
    color_sets = {
      "Dark Green": [(0, 0.10, 0.01), (0, 0.50, 0.05)],
      "Light Green": [(0, 0.50, 0.05), (0, 0.80, 0.08)],
      
      "Dark Cyan": [(0, 0.10, 0.10), (0, 0.50, 0.50)],
      "Light Cyan": [(0, 0.50, 0.50), (0, 0.80, 0.80)],
      
      "Dark Blue": [(0, 0.01, 0.10), (0, 0.05, 0.50)],
      "Light Blue": [(0, 0.05, 0.50), (0, 0.08, 0.80)],
      
      "Dark Magenta": [(0.08, 0, 0.10), (0.40, 0, 0.50)],
      "Light Magenta": [(0.40, 0, 0.50), (0.64, 0, 0.80)],
      
      "Dark Red": [(0.10, 0, 0), (0.50, 0, 0)],
      "Light Red": [(0.50, 0, 0), (0.80, 0, 0)],
      
      "Dark Orange": [(0.10, 0.02, 0), (0.50, 0.12, 0)],
      "Light Orange": [(0.50, 0.12, 0), (0.80, 0.19, 0)],
      
      "Dark Yellow": [(0.10, 0.09, 0), (0.50, 0.45, 0)],
      "Light Yellow": [(0.60, 0.43, 0), (0.80, 0.72, 0)],
      
      "Black": [(0,0,0), (0.35, 0.35,0.35)],
      "White": [(1.0,1.0,1.0), (0.7,0.7,0.7)],
    }
    
    for title, value in color_sets.items():
        
        color = arm.rigify_colors.add()
        color.name = title
        
        #set color by Color function of mathutils
        color.normal = Color(value[0])
        color.select = Color(value[1])
        color.active = Color(value[1])
        
    #Setup Bone Collection UI
    bone_col = {
      "Panels": ('Black', 1),
      "Sliders": ('Light Yellow', 2),
      "Frames": ('Black', 3),
      "Root": ('Purple', 5),
    }
    
    try:
        col = arm.collections.remove(arm.collections_all['Bones'])
    except:
        pass    
    
    for collection, (color, row) in bone_col.items():
        
        col = arm.collections.new(collection)
        col.rigify_color_set_name = color
        col.rigify_ui_row = row
        
    #Off Root Collection visibility by default
    arm.collections_all["Root"].is_visible = False
    
    #Switch Object Mode to Edit Mode
    if obj.mode != 'EDIT':
        bpy.ops.object.mode_set(mode='EDIT')    
    
    #Setup Sample Ui Bones: dict={name, head, tail, roll}
    edit_bone_list = {
    'face_frame': [(0.0, -5.543633108118229e-08, 5.6473917961120605), (0.0, -5.543633108118229e-08, 6.133790969848633), 0.0],
    'mouth': [(0.0, 0.0, 1.5499999523162842), (0.0, 0.0, 1.740804672241211), 0.0],
    'nostril.L': [(0.27000001072883606, 0.0, 2.930000066757202), (0.27000001072883606, 0.0, 3.119999885559082), 2.384185791015625e-07],
    'master_eyes': [(0.0, 0.0, 3.5999999046325684), (0.0, 0.0, 3.8499999046325684), 0.0],
    'eye.L': [(0.9100000262260437, 0.0, 3.5999999046325684), (0.9100000262260437, 0.0, 3.799999952316284), 0.0],
    'upper_mouth.L': [(0.21596229076385498, -6.121588569385494e-08, 2.0009925365448), (0.4703313112258911, -5.9033126831309346e-08, 2.5702366828918457), 0.42023468017578125],
    'upper_mouth.L.001': [(0.49028149247169495, -5.719165230289036e-08, 1.878411889076233), (0.664447546005249, -5.896283994388796e-08, 2.4770843982696533), 0.28310608863830566],
    'upper_mouth.L.002': [(0.7739555835723877, -1.1478326200631273e-07, 1.745539665222168), (1.1782857179641724, -9.988627169832398e-08, 2.2201547622680664), 0.7056026458740234],
    'mouth_side.L': [(0.9439049959182739, -1.5673393249926448e-07, 1.6007578372955322), (1.5610058307647705, -9.003208845115296e-08, 1.6898021697998047), 1.4274907112121582],
    'lower_mouth.L.002': [(0.7739555835723877, -7.28544051753488e-08, 1.4334733486175537), (1.1604664325714111, 7.154449122026563e-08, 0.944237470626831), 2.4729607105255127],
    'lower_mouth.L.001': [(0.48527011275291443, -1.5092740568434238e-07, 1.2655763626098633), (1.0132211446762085, -2.7697865334630478e-08, 0.9338986873626709), 2.1317191123962402],
    'lower_mouth.L': [(0.23694206774234772, -2.16923936591229e-07, 1.10234534740448), (0.33056363463401794, -5.543633108118229e-08, 0.48592227697372437), 2.990865707397461],
    'lower_nose.L': [(0.1394798308610916, -3.1118435828147994e-08, 2.555678129196167), (0.11152825504541397, 4.986545221186134e-08, 2.2549545764923096), -3.1415927410125732],
    'cheekbone.L': [(0.937404453754425, -1.0505499403734575e-07, 3.1059699058532715), (0.6727344989776611, -8.40231280108128e-08, 3.2514545917510986), -1.2217304706573486],
    'temple.L.001': [(1.635298728942871, -1.067702655177527e-07, 3.1187362670898438), (1.6292299032211304, -1.0676318140667718e-07, 3.4678308963775635), 0.0],
    'ear.L': [(2.001267671585083, -6.331668345183061e-08, 2.7953219413757324), (2.09895920753479, -6.22334184186002e-08, 3.3831419944763184), 0.1780235767364502],
    'master_blink': [(-0.11489725112915039, 9.37067312634099e-10, 3.974125385284424), (0.1351029872894287, 9.37067312634099e-10, 3.974125385284424), 1.570796251296997],
    'blink.L': [(0.9100000262260437, 1.7848774902518016e-08, 3.9364140033721924), (1.1600003242492676, 1.7848774902518016e-08, 3.9364140033721924), 1.570796251296997],
    'inner_lid.L': [(0.49135005474090576, 1.0597721811222982e-08, 3.8403708934783936), (0.49135005474090576, 2.5647791446203883e-08, 4.03971529006958), 0.0],
    'outer_lid.L': [(1.3318021297454834, 3.632682421539357e-08, 3.6488754749298096), (1.3856799602508545, 5.988302831383407e-08, 3.9608869552612305), 0.0872664600610733],
    'temple.L': [(1.5807512998580933, -2.1943947103864048e-07, 3.957305431365967), (1.5228856801986694, -1.390332045048126e-07, 3.6608808040618896), 3.3161256313323975],
    'inner_brow.L': [(0.33475422859191895, -3.3950863098652917e-07, 4.850950717926025), (0.17087438702583313, -1.6752261444707983e-07, 4.221416473388672), 3.3161256313323975],
    'brow.L': [(1.1901006698608398, -3.126360184069199e-07, 4.650944232940674), (0.562382161617279, -2.0229806807492423e-07, 4.480241298675537), 4.366734027862549],
    'forehead.L.001': [(1.0378299951553345, 0.0, 4.992839813232422), (1.2317099571228027, -3.5439356338429207e-07, 5.581544399261475), 0.3007551431655884],
    'forehead.L': [(0.44340598583221436, -0.00023348964168690145, 5.108238697052002), (0.5325449705123901, -0.00023348878312390298, 5.7216033935546875), 0.12693552672863007],
    'outer_brow.L': [(1.6323966979980469, 0.1054987981915474, 4.62101936340332), (1.5089484453201294, 0.10549893230199814, 4.146800518035889), 3.3161261081695557],
    'nostril.R': [(-0.27000001072883606, 0.0, 2.930000066757202), (-0.27000001072883606, 0.0, 3.119999885559082), -2.384185791015625e-07],
    'eye.R': [(-0.9100000262260437, 0.0, 3.5999999046325684), (-0.9100000262260437, 0.0, 3.799999952316284), -0.0],
    'upper_mouth.R': [(-0.21596229076385498, -6.121588569385494e-08, 2.0009925365448), (-0.4703313112258911, -5.9033126831309346e-08, 2.5702366828918457), -0.42023468017578125],
    'upper_mouth.R.001': [(-0.49028149247169495, -5.719165230289036e-08, 1.878411889076233), (-0.664447546005249, -5.896283994388796e-08, 2.4770843982696533), -0.28310608863830566],
    'upper_mouth.R.002': [(-0.7739555835723877, -1.1478326200631273e-07, 1.745539665222168), (-1.1782857179641724, -9.988627169832398e-08, 2.2201547622680664), -0.7056026458740234],
    'mouth_side.R': [(-0.9439049959182739, -1.5673393249926448e-07, 1.6007578372955322), (-1.5610058307647705, -9.003208845115296e-08, 1.6898021697998047), -1.4274907112121582],
    'lower_mouth.R.002': [(-0.7739555835723877, -7.28544051753488e-08, 1.4334733486175537), (-1.1604664325714111, 7.154449122026563e-08, 0.944237470626831), -2.4729607105255127],
    'lower_mouth.R.001': [(-0.48527011275291443, -1.5092740568434238e-07, 1.2655763626098633), (-1.0132211446762085, -2.7697865334630478e-08, 0.9338986873626709), -2.1317191123962402],
    'lower_mouth.R': [(-0.23694206774234772, -2.16923936591229e-07, 1.10234534740448), (-0.33056363463401794, -5.543633108118229e-08, 0.48592227697372437), -2.990865707397461],
    'lower_nose.R': [(-0.1394798308610916, -3.1118435828147994e-08, 2.555678129196167), (-0.11152825504541397, 4.986545221186134e-08, 2.2549545764923096), 3.1415927410125732],
    'cheekbone.R': [(-0.937404453754425, -1.0505499403734575e-07, 3.1059699058532715), (-0.6727344989776611, -8.40231280108128e-08, 3.2514545917510986), 1.2217304706573486],
    'temple.R.001': [(-1.635298728942871, -1.067702655177527e-07, 3.1187362670898438), (-1.6292299032211304, -1.0676318140667718e-07, 3.4678308963775635), -0.0],
    'ear.R': [(-2.001267671585083, -6.331668345183061e-08, 2.7953219413757324), (-2.09895920753479, -6.22334184186002e-08, 3.3831419944763184), -0.1780235767364502],
    'blink.R': [(-0.9100000262260437, 1.7848774902518016e-08, 3.9364140033721924), (-1.1600003242492676, 1.7848774902518016e-08, 3.9364140033721924), -1.570796251296997],
    'inner_lid.R': [(-0.49135005474090576, 1.0597721811222982e-08, 3.8403708934783936), (-0.49135005474090576, 2.5647791446203883e-08, 4.03971529006958), -0.0],
    'outer_lid.R': [(-1.3318021297454834, 3.632682421539357e-08, 3.6488754749298096), (-1.3856799602508545, 5.988302831383407e-08, 3.9608869552612305), -0.0872664600610733],
    'temple.R': [(-1.5807512998580933, -2.1943947103864048e-07, 3.957305431365967), (-1.5228856801986694, -1.390332045048126e-07, 3.6608808040618896), -3.3161256313323975],
    'inner_brow.R': [(-0.33475422859191895, -3.3950863098652917e-07, 4.850950717926025), (-0.17087438702583313, -1.6752261444707983e-07, 4.221416473388672), -3.3161256313323975],
    'brow.R': [(-1.1901006698608398, -3.126360184069199e-07, 4.650944232940674), (-0.562382161617279, -2.0229806807492423e-07, 4.480241298675537), -4.366734027862549],
    'forehead.R.001': [(-1.0378299951553345, 0.0, 4.992839813232422), (-1.2317099571228027, -3.5439356338429207e-07, 5.581544399261475), -0.3007551431655884],
    'forehead.R': [(-0.44340598583221436, -0.00023348964168690145, 5.108238697052002), (-0.5325449705123901, -0.00023348878312390298, 5.7216033935546875), -0.12693552672863007],
    'outer_brow.R': [(-1.6323966979980469, 0.1054987981915474, 4.62101936340332), (-1.5089484453201294, 0.10549893230199814, 4.146800518035889), -3.3161261081695557],
}
    
    created_bones = []
    
    #Create Bones and Setup in Edit Mode
    for name, (head, tail,roll) in edit_bone_list.items():
        
        bone = arm.edit_bones.new(name)
        bone.head = head
        bone.tail = tail
        bone.roll = roll
        
        arm.collections_all['Panels'].assign(bone)
        created_bones.append(bone)

    #Create Bones and Setup in Edit Mode
    for name, (head, tail,roll) in edit_bone_list.items():
        if name != 'face_frame':
            arm.edit_bones[name].parent = arm.edit_bones['face_frame']
    
    #Switch Object Mode to Edit Mode
    if obj.mode != 'POSE':
        bpy.ops.object.mode_set(mode='POSE')
        
    #Pose Bones list: dict = {name, slider_type, minimal, clamp, fill_01, fill_02}
    pose_bone_list = {
        
        'mouth': ['LARGE', False, 'NONE', True, True], 
        'master_eyes': ['LARGE', False, 'NONE', True, True], 
        'master_blink': ['SMALL', True, 'UP', True, False], 
         
        'nostril.L': ['LARGE', False, 'NONE', True, True],  
        'eye.L': ['LARGE', False, 'NONE', True, True], 
        'upper_mouth.L': ['SMALL', True, 'UP', True, False],
        'upper_mouth.L.001': ['SMALL', True, 'UP', True, False],
        'upper_mouth.L.002': ['SMALL', True, 'UP', True, False], 
        'mouth_side.L': ['SMALL', True, 'UP', True, False],
        'lower_mouth.L.002': ['SMALL', True, 'UP', True, False],
        'lower_mouth.L.001': ['SMALL', True, 'UP', True, False],
        'lower_mouth.L': ['SMALL', True, 'UP', True, False], 
        'lower_nose.L': ['SMALL', True, 'UP', True, False],
        'cheekbone.L': ['SMALL', True, 'UP', True, False], 
        'temple.L.001': ['SMALL', True, 'UP', True, False],
        'ear.L': ['SMALL', True, 'UP', True, False],
        'blink.L': ['SMALL', True, 'NONE', True, False], 
        'inner_lid.L': ['SMALL', True, 'NONE', True, False],
        'outer_lid.L': ['SMALL', True, 'NONE', True, False],
        'temple.L': ['SMALL', True, 'UP', True, False],
        'inner_brow.L': ['SMALL', True, 'UP', True, False], 
        'brow.L': ['SMALL', True, 'UP', True, False],
        'outer_brow.L': ['SMALL', True, 'UP', True, False],
        'forehead.L.001': ['SMALL', True, 'UP', True, False],
        'forehead.L': ['SMALL', True, 'UP', True, False],
        
        'nostril.R': ['LARGE', False, 'NONE', True, True],  
        'eye.R': ['LARGE', False, 'NONE', True, True], 
        'upper_mouth.R': ['SMALL', True, 'UP', True, False],
        'upper_mouth.R.001': ['SMALL', True, 'UP', True, False],
        'upper_mouth.R.002': ['SMALL', True, 'UP', True, False], 
        'mouth_side.R': ['SMALL', True, 'UP', True, False],
        'lower_mouth.R.002': ['SMALL', True, 'UP', True, False],
        'lower_mouth.R.001': ['SMALL', True, 'UP', True, False],
        'lower_mouth.R': ['SMALL', True, 'UP', True, False], 
        'lower_nose.R': ['SMALL', True, 'UP', True, False],
        'cheekbone.R': ['SMALL', True, 'UP', True, False], 
        'temple.R.001': ['SMALL', True, 'UP', True, False],
        'ear.R': ['SMALL', True, 'UP', True, False],
        'blink.R': ['SMALL', True, 'NONE', True, False], 
        'inner_lid.R': ['SMALL', True, 'NONE', True, False],
        'outer_lid.R': ['SMALL', True, 'NONE', True, False],
        'temple.R': ['SMALL', True, 'UP', True, False],
        'inner_brow.R': ['SMALL', True, 'UP', True, False], 
        'brow.R': ['SMALL', True, 'UP', True, False],
        'outer_brow.R': ['SMALL', True, 'UP', True, False],
        'forehead.R.001': ['SMALL', True, 'UP', True, False],
        'forehead.R': ['SMALL', True, 'UP', True, False],
    }
        
    for name, (slider_type, minimal, clamp, fill_slider, fill_pan) in pose_bone_list.items():
        
        bone = obj.pose.bones[name]
        
        bone.rigify_type = "ui.slider"
        bone.rigify_parameters.slider_type = slider_type
        bone.rigify_parameters.minimal_design = minimal
        bone.rigify_parameters.clamp_up_down = clamp
        bone.rigify_parameters.fill_slider = fill_slider
        bone.rigify_parameters.fill_pan = fill_pan

        bone.rigify_parameters.relink_constraints = True
        bone.rigify_parameters.parent_bone = 'face_frame'
        
        bone.rigify_parameters.slider_layers_extra = True
        bone.rigify_parameters.slider_coll_refs.add()
        bone.rigify_parameters.slider_coll_refs[0].set_collection(arm.collections_all['Sliders'])
    
    #setup Frame Bone
    frame_bone = obj.pose.bones['face_frame']
    frame_bone.rigify_type = "ui.frame"
    frame_bone.rigify_parameters.title = True
    frame_bone.rigify_parameters.custom_title = 'Face UI'
    
    #Switch Object Mode to Edit Mode
    if obj.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
            
    return created_bones

if __name__ == "__main__":
    create(bpy.context.active_object)