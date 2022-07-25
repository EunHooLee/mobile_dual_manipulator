// Auto-generated. Do not edit!

// (in-package ethercat_test.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class trajectory {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.traj = null;
    }
    else {
      if (initObj.hasOwnProperty('traj')) {
        this.traj = initObj.traj
      }
      else {
        this.traj = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type trajectory
    // Serialize message field [traj]
    bufferOffset = _arraySerializer.float64(obj.traj, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type trajectory
    let len;
    let data = new trajectory(null);
    // Deserialize message field [traj]
    data.traj = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.traj.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'ethercat_test/trajectory';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2c706e3135da03d0b3079ab165a03313';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] traj
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new trajectory(null);
    if (msg.traj !== undefined) {
      resolved.traj = msg.traj;
    }
    else {
      resolved.traj = []
    }

    return resolved;
    }
};

module.exports = trajectory;
