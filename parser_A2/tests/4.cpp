
// /*
// Returns the object ID.  -1 (invalid), 0, 1 - reserved
// */
// long find_object_id(const char *key, struct objfs_state *objfs)
// {
//     return -1;   
// }

// /*
//   Creates a new object with obj.key=key. Object ID must be >=2.
//   Must check for duplicates.

//   Return value: Success --> object ID of the newly created object
//                 Failure --> -1
// */
// long create_object(const char *key, struct objfs_state *objfs)
// {
//    return -1;
// }
// /*
//   One of the users of the object has dropped a reference
//   Can be useful to implement caching.
//   Return value: Success --> 0
//                 Failure --> -1
// */
// long release_object(int objid, struct objfs_state *objfs)
// {
//     return 0;
// }

// /*
//   Destroys an object with obj.key=key. Object ID is ensured to be >=2.

//   Return value: Success --> 0
//                 Failure --> -1
// */
// long destroy_object(const char *key, struct objfs_state *objfs)
// {
//     return -1;
// }

// /*
//   Renames a new object with obj.key=key. Object ID must be >=2.
//   Must check for duplicates.  
//   Return value: Success --> object ID of the newly created object
//                 Failure --> -1
// */

// long rename_object(const char *key, const char *newname, struct objfs_state *objfs)
// {
   
//    return -1;
// }

// /*
//   Writes the content of the buffer into the object with objid = objid.
//   Return value: Success --> #of bytes written
//                 Failure --> -1
// */
// long objstore_write(int objid, const char *buf, int size, struct objfs_state *objfs)
// {
//    return -1;
// }

// /*
//   Reads the content of the object onto the buffer with objid = objid.
//   Return value: Success --> #of bytes written
//                 Failure --> -1
// */
// long objstore_read(int objid, char *buf, int size, struct objfs_state *objfs)
// {
//    return -1;
// }

// /*
//   Reads the object metadata for obj->id = buf->st_ino
//   Fillup buf->st_size and buf->st_blocks correctly
//   See man 2 stat 
// */
// int fillup_size_details(struct stat *buf)
// {
//    return -1;
// }

// /*
//    Set your private pointeri, anyway you like.
// */
// int objstore_init(struct objfs_state *objfs)
// {
//    dprintf("Done objstore init\n");
//    return 0;
// }

/*
   Cleanup private data. FS is being unmounted
*/
int objstore_destroy(struct objfs_state *objfs)
{
   dprintf("Done objstore destroy\n");
   return 0;
}
