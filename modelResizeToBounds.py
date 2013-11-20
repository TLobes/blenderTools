import bpy, sys
from datetime import datetime
 
try:
	dt = datetime.now()
	start_time = dt;
	print('%s.%0.3d' % (dt.strftime('%Y%m%d_%H%M%S'), dt.microsecond/1000),
	"start time")
  
  # code snippet from larger model staging file
  bpy.ops.object.mode_set(mode = 'OBJECT')	
 
	bounding_box = imported_object.bound_box;
	
	point=bounding_box[0] 
	min_x=point[0] 
	max_x=point[0] 
	min_y=point[1] 
	max_y=point[1] 
	min_z=point[2] 
	max_z=point[2] 
	
	#find min/max values 
	for point in bounding_box: 
		if min_x>point[0]: min_x=point[0] 
		if max_x<point[0]: max_x=point[0] 
		if min_y>point[1]: min_y=point[1] 
		if max_y<point[1]: max_y=point[1] 
		if min_z>point[2]: min_z=point[2] 
		if max_z<point[2]: max_z=point[2] 
	
	if (file_type == "wrl"):
		# vrml is yup so account for object matrix transform
		tmin = min_y
		tmax = max_y
		min_y = min_z
		max_y = max_z
		min_z = tmin
		max_z = tmax
		
	size_x = abs( max_x - min_x )
	size_y = abs( max_y - min_y )
	size_z = abs( max_z - min_z )
 
	# schaal naar 1x1x1
	size_max = 1000
	if size_x>size_max: size_max=size_x
	if size_y>size_max: size_max=size_y
	if size_z>size_max: size_max=size_z
 
	#size = 4
 
	# fit the model in a shoebox
	size_max_x = 6
	size_max_y = 6
	size_max_z = 4
 
	# determine along wich axis we need to scale our object
	dt = datetime.now()
 
	if size_x / size_max_x > size_z / size_max_z:
		size = size_max_x
		sr = size_x / size_max_x
		sm = size_x
		print("SIZE: Select X")
	else:
		size = size_max_z
		sr = size_z / size_max_z
		sm = size_z
		print("SIZE: Select Z")
 
	if sr < size_y / size_max_y:
		size = size_max_y
		sm = size_y
		dt = datetime.now()
		print('%s.%0.3d' % (dt.strftime('%Y%m%d_%H%M%S'), dt.microsecond/1000),
		"SIZE: Select Y")
 
	dt = datetime.now()
	print("Size = ", size)	
	print("Sm = ", sm)
 
	size_factor = size/sm
 
	print("before size x:", size_x)
	print("before size y:", size_y)
	print("before size z:", size_z)
	print("size_factor", size_factor)
 
	imported_object.scale = [size_factor,size_factor,size_factor];
 
	min_x = min_x * size_factor
	min_y = min_y * size_factor
	min_z = min_z * size_factor
 
	max_x = max_x * size_factor
	max_y = max_y * size_factor
	max_z = max_z * size_factor
 
	print("min_x=", min_x, " max_x=", max_x)
	print("min_y=", min_y, " max_y=", max_y)
	print("min_z=", min_z, " max_z=", max_z)
 
	center_x =  ( max_x + min_x ) /2 
	center_y =  ( max_y + min_y ) /2 
	center_z =  ( max_z + min_z ) /2 
 
	print("center_x: ", center_x)
	print("center_y: ", center_y)
	print("center_z: ", center_z)
 
	zloc = ( max_z - min_z )/2 - center_z
	imported_object.location = [-center_x, -center_y, zloc]
 
	plane_max = max(size_x, size_y);
	
	# Adjust viewport size to aspect ratio to keep high non background pixels and faster rendering
	adjust_viewport = True
	if (adjust_viewport):
		render_x = 1024
		render_y = 1024
 
		if (size_z > plane_max):
			ratio = plane_max / size_z
			if (ratio <= 0.5):
				# move camera closer
				bpy.data.objects['Camera'].location.z = 10.2
				print("Move camera closer")
		else:
			ratio = size_z / plane_max
			if (ratio <= 0.5):
				# move camera closer
				bpy.data.objects['Camera'].location.z = 10.2
				print("Move camera closer")
 
		bpy.context.scene.render.resolution_x = render_x
		bpy.context.scene.render.resolution_y = render_y
		print("ratio: ", ratio, " x: ", render_x, " y: ", render_y)
	
	
	bpy.context.scene.render.filepath
	bpy.data.scenes[0].update()
	#end snippet from larger model staging file
	
except:
	print("Error Caught")	
	sys.exit(100)
	