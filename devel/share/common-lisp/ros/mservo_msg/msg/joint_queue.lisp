; Auto-generated. Do not edit!


(cl:in-package mservo_msg-msg)


;//! \htmlinclude joint_queue.msg.html

(cl:defclass <joint_queue> (roslisp-msg-protocol:ros-message)
  ((jointq
    :reader jointq
    :initarg :jointq
    :type (cl:vector mservo_msg-msg:joint_data)
   :initform (cl:make-array 2 :element-type 'mservo_msg-msg:joint_data :initial-element (cl:make-instance 'mservo_msg-msg:joint_data))))
)

(cl:defclass joint_queue (<joint_queue>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <joint_queue>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'joint_queue)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mservo_msg-msg:<joint_queue> is deprecated: use mservo_msg-msg:joint_queue instead.")))

(cl:ensure-generic-function 'jointq-val :lambda-list '(m))
(cl:defmethod jointq-val ((m <joint_queue>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mservo_msg-msg:jointq-val is deprecated.  Use mservo_msg-msg:jointq instead.")
  (jointq m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <joint_queue>) ostream)
  "Serializes a message object of type '<joint_queue>"
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'jointq))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <joint_queue>) istream)
  "Deserializes a message object of type '<joint_queue>"
  (cl:setf (cl:slot-value msg 'jointq) (cl:make-array 2))
  (cl:let ((vals (cl:slot-value msg 'jointq)))
    (cl:dotimes (i 2)
    (cl:setf (cl:aref vals i) (cl:make-instance 'mservo_msg-msg:joint_data))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<joint_queue>)))
  "Returns string type for a message object of type '<joint_queue>"
  "mservo_msg/joint_queue")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'joint_queue)))
  "Returns string type for a message object of type 'joint_queue"
  "mservo_msg/joint_queue")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<joint_queue>)))
  "Returns md5sum for a message object of type '<joint_queue>"
  "975ac8b6c2831749c6d3e61906fa26d9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'joint_queue)))
  "Returns md5sum for a message object of type 'joint_queue"
  "975ac8b6c2831749c6d3e61906fa26d9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<joint_queue>)))
  "Returns full string definition for message of type '<joint_queue>"
  (cl:format cl:nil "joint_data[2] jointq~%~%================================================================================~%MSG: mservo_msg/joint_data~%int32[7] pos~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'joint_queue)))
  "Returns full string definition for message of type 'joint_queue"
  (cl:format cl:nil "joint_data[2] jointq~%~%================================================================================~%MSG: mservo_msg/joint_data~%int32[7] pos~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <joint_queue>))
  (cl:+ 0
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'jointq) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <joint_queue>))
  "Converts a ROS message object to a list"
  (cl:list 'joint_queue
    (cl:cons ':jointq (jointq msg))
))
