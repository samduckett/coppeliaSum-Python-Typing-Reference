# cSpell: ignore
from typing import Protocol, Tuple, List, Any, overload


class SimAPI(Protocol):
    # Auto-generated Python stubs from CoppeliaSim manual

    def acquireLock(self) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAcquireLock.htm Allows to
        have CoppeliaSim wait for a threaded code section to be executed without
        interruption. Locking is cumulative

        """
        ...

    def addDrawingObject(
        self,
        objectType: int,
        size: float,
        duplicateTolerance: float,
        parentObjectHandle: int,
        maxItemCount: int,
        color: list,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAddDrawingObject.htm Adds
        a drawing object that will be displayed in the scene. Drawing objects are
        containers that hold several items of a given type. This can be used for
        several different applications (simulation of paint, simulation of welding
        seam, display of 3D objects, etc.). Drawing objects created in a  simulation
        script  will be automatically removed at simulation end

        Args:
            objectType (int): a
            size (float): size of the item (width of lines or size of points are in pixels, other sizes are in meters
            duplicateTolerance (float): if different from 0.0, then a call to
            parentObjectHandle (int): handle of the scene object where the drawing items should keep attached to (if the scene object moves, the drawing items will also move), or -1 if the drawing items are relative to the world (fixed)
            maxItemCount (int): maximum number of items this object can hold. 0 uses a default size of 1000.
            color (list): default color (3 rgb values). Can be None/nil

        Returns:
            drawingObjectHandle (int): No detailed return description.

        """
        ...

    def addDrawingObjectItem(
        self, drawingObjectHandle: int, itemData: list
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAddDrawingObjectItem.htm
        Adds an item (or clears all items) to a previously inserted drawing object

        Args:
            drawingObjectHandle (int): handle of a previously added drawing object. Can be combined with sim.handleflag_addmultiple to add several drawing items at once, or with sim.handleflag_codedstring, when one wishes to provide data as a float buffer
            itemData (list): data relative to an item. If the item is a point item, 3 values are required [x y z]. If the item is a line item, 6 values are required, etc. None/nil to empty the drawing object

        Returns:
            result (int): If the point was added, the return value is >0, if it was not added the return value is 0

        """
        ...

    def addForce(self, shapeHandle: int, position: list, force: list) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAddForce.htm Adds a non-
        central force to a shape object that is dynamically enabled. Added forces
        are cumulative, applied relative to the center of mass, and are reset to
        zero after  sim.handleDynamics was called (or by using the following flag:
        sim.handleflag_resetforcetorque)

        Args:
            shapeHandle (int): handle of a dynamically enabled shape. Can be combined with sim.handleflag_resetforcetorque in order to clear the accumulated force and torque.
            position (list): array of 3 values that represent the relative position where the force should be applied.
            force (list): array of 3 values that represent the force (in relative coordinates) to add.

        """
        ...

    def addForceAndTorque(
        self, shapeHandle: int, force: list, torque: list
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAddForceAndTorque.htm
        Adds a force and/or torque to a shape object that is dynamically enabled.
        Forces are applied at the center of mass. Added forces and torques are
        cumulative, and are reset to zero after  sim.handleDynamics  was called (or
        by using the following flags: sim.handleflag_resetforce and/or
        sim.handleflag_resettorque)

        Args:
            shapeHandle (int): handle of a dynamically enabled shape. Can be combined with sim.handleflag_resetforce and/or sim.handleflag_resettorque in order to clear the accumulated force or torque.
            force (list): array of 3 values that represent the force (in absolute coordinates) to add. Can be None/nil
            torque (list): array of 3 values that represent the torque (in absolute coordinates) to add. Can be None/nil

        """
        ...

    def addGraphCurve(
        self,
        graphHandle: int,
        curveName: str,
        dim: int,
        streamIds: list,
        defaultValues: list,
        unitStr: str,
        options: int,
        color: list,
        curveWidth: int,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAddGraphCurve.htm Adds or
        updates a graph curve. A graph curve is persistent, but can be removed with
        sim.destroyGraphCurve

        Args:
            graphHandle (int): handle of the graph
            curveName (str): name of the curve
            dim (int): dimension of the curve. Valid values are 2 or 3
            streamIds (list): array of 2 or 3 graph streams (x/y curves require 2 stream IDs, xyz curves require 3 stream IDs). Indicate -1 for a missing stream, in which case a default value will be used instead
            defaultValues (list): array of 2 or 3 default values
            unitStr (str): str describing the unit of the curve. Can be None/nil
            options (int): bit-coded:
            color (list): rgb-triplet, with values between 0.0 and 1.0, indicating the color of the stream. Can be None/nil
            curveWidth (int): the width of an xyz curve

        Returns:
            curveId (int): id of the created/updated curve

        """
        ...

    def addGraphStream(
        self,
        graphHandle: int,
        streamName: str,
        unitStr: str,
        options: int,
        color: list,
        cyclicRange: Any = 0,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAddGraphStream.htm Adds
        or updates a graph stream. A graph stream is persistent, but can be removed
        with  sim.destroyGraphCurve

        Args:
            graphHandle (int): handle of the graph
            streamName (str): name of the stream
            unitStr (str): str describing the unit of the stream. Can be None/nil
            options (int): bit-coded:
            color (list): rgb-triplet, with values between 0.0 and 1.0, indicating the color of the stream. Can be None/nil
            cyclicRange = 0 (Any):  can be used with cyclic values (e.g. angles) for correct data interpretation during stream data transformation. Set to 0 if not used

        Returns:
            streamId (int): id of the created/updated stream

        """
        ...

    def addItemToCollection(
        self, collectionHandle: int, what: int, objectHandle: int, options: int
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAddItemToCollection.htm
        Adds an item to a  collection

        Args:
            collectionHandle (int): handle of a collection.
            what (int): type of object (or group of objects) to add. Following are allowed values:
            objectHandle (int): handle of an object
            options (int): bit-coded options:

        """
        ...

    def addLog(self, verbosity: int, message: str) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAddLog.htm Adds a log
        message that will be output in the console or status bar

        Args:
            verbosity (int): the
            message (str): the message. None/nil clears the status bar

        """
        ...

    def addParticleObject(
        self,
        objectType: int,
        size: float,
        density: float,
        parameters: list,
        lifeTime: float,
        maxItemCount: int,
        color: list,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAddParticleObject.htm
        Adds a particle object that will be simulated and displayed in the scene.
        Particle objects are containers that hold several items (particles) of a
        given type. This can be used for several different applications (e.g.
        simulation of air/water jets)

        Args:
            objectType (int): a
            size (float): diameter of the particles (spheres)
            density (float): density of the particles
            parameters (list): an array of values, allowing to specify additional parameters. Can be None/nil. Values come in pair (an integer indicating what parameter, and a float indicating the parameter value. Following indicates the parameters:
            lifeTime (float): simulation time after which the particles are destroyed. Set to 0.0 for an unlimited lifetime.
            maxItemCount (int): the maximum number of particles that this object can hold
            color (list): default ambient/diffuse color (pointer to 3 rgb values). Can be None/nil

        Returns:
            particleObjectHandle (int): No detailed return description.

        """
        ...

    def addParticleObjectItem(
        self, particleObjectHandle: int, itemData: list
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAddParticleObjectItem.htm
        Adds an item (or clears all items) to a previously inserted particle object

        Args:
            particleObjectHandle (int): handle of a previously added particle object
            itemData (list): data relative to an item. All items (particles) require at least 6 values:ï¿½p1x, p1y, p1z, p2x, p2y, p2z with p1 is the particle start position, p2-p1 is the particle initial velocity vector. Auxiliary values might be required depending on the particle object attributes. See the

        """
        ...

    def adjustView(
        self,
        viewHandleOrIndex: int,
        objectHandle: int,
        options: int,
        viewLabel: str,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAdjustView.htm Adjusts
        parameters of a view

        Args:
            viewHandleOrIndex (int): handle of the view (can also be a floating view), or the index of the view.
            objectHandle (int): handle of the object that you wish to associate with the view. Must be a viewable object. Can also be -1, in which case the view is emptied
            options (int): bit-coded:
            viewLabel (str): a label that will be displayed at the top of a floating view. If None/nil is specified, then the name of the associated viewable object is taken as label.

        Returns:
            res (int): a value >0 in case of success

        """
        ...

    def alignShapeBB(self, shapeHandle: int, pose: list) -> bool:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAlignShapeBB.htm
        Reorients the bounding box of a shape, while keeping the shape frame in
        place. The shape's inertia properties are unaffected

        Args:
            shapeHandle (int): handle of the shape
            pose (list): pose describing the new orientation of the shape's bounding box. The pose is expressed as [x y z qx qy qz qw], where the positional part is ignored. A pose containing only zeros aligns the bounding box with the mesh's natural bounding box

        Returns:
            result (bool): 0 if the bounding box could not be reoriented (the bounding box of primitive shapes cannot be reoriented), otherwise 1.

        """
        ...

    def alphaBetaGammaToYawPitchRoll(
        self, alpha: float, beta: float, gamma: float
    ) -> Tuple[float, float, float]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAlphaBetaGammaToYawPitchR
        oll.htm Converts CoppeliaSim's alpha-beta-gamma angles to Yaw-Pitch-Roll
        angles

        Args:
            alpha (float): the alpha angle
            beta (float): the beta angle
            gamma (float): the gamma angle

        Returns:
            yaw (float): the yaw angle
            pitch (float): the pitch angle
            roll (float): the roll angle

        """
        ...

    def announceSceneContentChange(self) -> int:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simAnnounceSceneContentChange.htm
        Announces a change in the scene. This is required for the undo/redo function
        to operate properly when performing changes via the API. Only call this
        function directly after a change was made through a dialog element (e.g. a
        checkbox was checked/unchecked) and that change was reported to the scene.
        What this call will do is following: the whole scene will be serialized
        (saved) to memory as a "scene image" and compared to a previously memorized
        "scene image". If both images are same, then the last image is discarded,
        otherwise only the changes between the two images are memorized. A call to
        this function has no effect (and doesn't generate any error) when called
        during simulation or when in edit mode.

        Returns:
            result (int): No detailed return description.

        """
        ...

    def auxiliaryConsoleClose(self, consoleHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsoleClose.htm
        Closes an auxiliary console window

        Args:
            consoleHandle (int): handle of the console window, previously returned by sim.auxiliaryConsoleOpen

        Returns:
            result (int): 0 if the console doesn't exist (anymore), in which case no error is generated. 1 if the console window was closed

        """
        ...

    def auxiliaryConsoleOpen(
        self,
        title: str,
        maxLines: int,
        mode: int,
        position: list,
        size: list,
        textColor: list,
        backgroundColor: list,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsoleOpen.htm
        Opens an auxiliary console window for text display. This console window is
        different from the application main console window. Console window handles
        are shared across all simulator scenes

        Args:
            title (str): title of the console window
            maxLines (int): number of text lines that can be displayed and buffered
            mode (int): bit-coded value:
            position (list): initial position of the console window (x and y value). Can be None/nil
            size (list): initial size of the console window (x and y value). Can be None/nil
            textColor (list): color of the text (rgb values, 0.0 - 1.0). Can be None/nil
            backgroundColor (list): background color of the console window (rgb values, 0.0 - 1.0 ). Can be None/nil

        Returns:
            consoleHandle (int): console window handle

        """
        ...

    def auxiliaryConsolePrint(self, consoleHandle: int, text: str) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsolePrint.htm
        Prints to an auxiliary console window

        Args:
            consoleHandle (int): handle of the console window, previously returned by the
            text (str): text to append, or None/nil to clear the console window

        Returns:
            result (int): 0 if the console doesn't exist (anymore), in which case no error is generated. 1 if the operation was successful

        """
        ...

    def auxiliaryConsoleShow(self, consoleHandle: int, showState: bool) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simAuxiliaryConsoleShow.htm
        Shows or hides an auxiliary console window

        Args:
            consoleHandle (int): handle of the console window, previously returned by
            showState (bool): indicates whether the console should be hidden (0) or shown (!=0)

        Returns:
            result (int): 0 if the console doesn't exist (anymore), in which case no error is generated. 1 if the console window's show state was changed.

        """
        ...

    def broadcastMsg(self, message: dict, options: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simBroadcastMsg.htm
        Broadcasts a message to all scripts, except for the emitting script.
        Messages are received synchronously via the sysCall_msg  callback function

        Args:
            message (dict): message to broadcast. Best is to use following skeleton message: message = {'id': 'msgIdentifyingstr', 'data': [...]}
            options (int): not used, keep at 0

        """
        ...

    def buildMatrix(self, position: list, eulerAngles: list) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simBuildMatrix.htm Builds a
        transformation matrix based on a position vector and Euler angles

        Args:
            position (list): array of 3 values
            eulerAngles (list): array of 3 values

        Returns:
            matrix (list): array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]

        """
        ...

    def buildPose(
        self, position: list, eulerAnglesOrAxis: list, mode: int, axis2: list
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simBuildPose.htm Builds a
        pose based on a position vector and  Euler angles  or axes

        Args:
            position (list): pointer to 3 values representing the position component
            eulerAnglesOrAxis (list): pointer to 3 values representing Euler angles or a reference frame axis (see mode below)
            mode (int): describes how the orientation is specified:

                0: eulerAnglesOrAxis1 represents Euler angles and axis2 is ignored
                1: eulerAnglesOrAxis1 represents the x-axis of the new pose's reference frame, axis2 is ignored
                2: eulerAnglesOrAxis1 represents the y-axis of the new pose's reference frame, axis2 is ignored
                3: eulerAnglesOrAxis1 represents the z-axis of the new pose's reference frame, axis2 is ignored
                4: eulerAnglesOrAxis1 represents the x-axis and axis2 represents the y-axis of the new pose's reference frame
                5: eulerAnglesOrAxis1 represents the y-axis and axis2 represents the z-axis of the new pose's reference frame
                6: eulerAnglesOrAxis1 represents the z-axis and axis2 represents the x-axis of the new pose's reference frame
                7: eulerAnglesOrAxis1 represents the x-axis and axis2 represents the z-axis of the new pose's reference frame
                8: eulerAnglesOrAxis1 represents the y-axis and axis2 represents the x-axis of the new pose's reference frame
                9: eulerAnglesOrAxis1 represents the z-axis and axis2 represents the y-axis of the new pose's reference frame

            axis2 (list): pointer to 3 values representing a reference frame axis (see mode above)

        Returns:
            pose (list): the pose (array of 7 values [x y z qx qy qz qw])

        """
        ...

    def callScriptFunction(
        self, functionName: str, scriptHandle: int, *args
    ) -> Any:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCallScriptFunction.htm
        Calls a script function (from a  plugin ,  the main client application , or
        from another script). This represents a  user callback  inside of a script.
        The target script must be initialized for this call to succeed, e.g. when
        calling  simulation scripts , then simulation must be running

        Args:
            functionName (str): the function to call.
            scriptHandle (int): the handle of the script, or sim.handle_self to target the current script. See
            *args (Any): any number of arguments that will be handed over to the called function

        Returns:
            ... (Any): any number of return values from the called function.

        """
        ...

    def cameraFitToView(
        self,
        viewHandleOrIndex: int,
        objectHandles: list,
        options: int,
        scaling: float,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCameraFitToView.htm
        Shifts and adjusts a camera associated with a view to fill the view entirely
        with the specified objects or models

        Args:
            viewHandleOrIndex (int): handle of the view (can also be a floating view), or the index of the view. If the camera is not associated with any view, then you can specify the handle of the camera, together with the
            objectHandles (list): object handles. Only visible objects will be taken into account. Can be None/nil, in which case the whole visible scene will be filling the view.
            options (int): bit-coded:
            scaling (float): scaling factor. Use 1.0 for normal behaviour.

        Returns:
            result (int): 0 for a silent error (e.g. when the indicated view doesn't exist anymore), 1 for success

        """
        ...

    def cancelScheduledExecution(self, id: int) -> bool:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simCancelScheduledExecution.htm
        Cancels a scheduled execution of a function

        Args:
            id (int): id of the scheduled execution function

        Returns:
            canceled (bool): cancelation status

        """
        ...

    def changeEntityColor(
        self, entityHandle: int, newColor: list, colorComponent: int
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simChangeEntityColor.htm
        Changes the color of an  entity , and returns its original color. Currently
        only takes into account  collections and  shapes

        Args:
            entityHandle (int): handle of a entity
            newColor (list): array of 3 rgb values, each between 0.0 and 1.0
            colorComponent (int): a

        Returns:
            originalColorData (list): original color data, to be used as argument with

        """
        ...

    def checkCollision(
        self, entity1Handle: int, entity2Handle: int
    ) -> Tuple[int, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCheckCollision.htm Checks
        whether two entities are colliding. The collidable flags of the entities are
        overridden if the entities are objects. If the entities are both the same
        collection (i.e. with the same collection handle), then same objects will
        not be checked against themselve

        Args:
            entity1Handle (int): handle of entity 1 (can be an object handle or a collection handle)
            entity2Handle (int): handle of entity 2 (can be an object handle or a collection handle), or sim.handle_all to check entity1 against all other collidable objects

        Returns:
            result (int): 0 or 1 to indicate a collision state
            collidingObjectHandles (list): array containing the colliding pair

        """
        ...

    def checkCollisionEx(
        self, entity1Handle: int, entity2Handle: int
    ) -> Tuple[int, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCheckCollisionEx.htm
        Checks whether two entities are colliding, and will return all intersections
        between the two entities. The collidable flags of the entities are
        overridden if the entities are objects

        Args:
            entity1Handle (int): handle of entity 1 (can be an object handle or a collection handle)
            entity2Handle (int): handle of entity 2 (can be an object handle or a collection handle), or sim.handle_all to check entity1 against all other collidable objects

        Returns:
            result (int): number of segments returned
            intersections (list): array containing the intersection segments between the two entities

        """
        ...

    def checkDistance(
        self, entity1Handle: int, entity2Handle: int, threshold: float
    ) -> Tuple[int, list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCheckDistance.htm Checks
        the minimum distance between two entities. The measurable flags of the
        entities are overridden if the entities are objects. If the entities are
        both the same collection (i.e. with the same collection handle), then same
        objects will not be checked against themselve

        Args:
            entity1Handle (int): handle of entity 1 (can be an object handle or a collection handle)
            entity2Handle (int): handle of entity 2 (can be an object handle or a collection handle), or sim.handle_all to check entity1 against all other measurable objects
            threshold (float): if distance is bigger than the threshold, the distance is not calculated and result is 0. If threshold is 0 or negative, then no threshold is used.

        Returns:
            result (int): 1 if distance is smaller than the threshold
            distanceData (list): array of 7 values: [obj1X obj1Y obj1Z obj2X obj2Y obj2Z dist]
            objectHandlePair (list): array of 2 object handles representing the two objects that hold the minimum distance segmen

        """
        ...

    def checkOctreePointOccupancy(
        self, octreeHandle: int, options: int, points: list
    ) -> Tuple[int, int, int, int]:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simCheckOctreePointOccupancy.htm
        Checks whether the provided points collide with the  OC tree  voxels

        Args:
            octreeHandle (int): handle of the OC tree
            options (int): bit-coded:
            points (list): points specified as x/y/z coordinates

        Returns:
            res (int): 0 if the points do not collide with the voxels, 1 if the points collide with the voxels
            tag (int): tag value of the voxel that collides with a single point. If several points are tested, this return value should be ignored
            locLow (int): value specifying the location of the voxel that collides with a single point. If several points are tested, then this return value should be ignored
            locHigh (int): value specifying the location of the voxel that collides with a single point. If several points are tested, then this return value should be ignored

        """
        ...

    def checkProximitySensor(
        self, sensorHandle: int, entityHandle: int
    ) -> Tuple[int, float, list, int, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCheckProximitySensor.htm
        Checks whether the proximity sensor detects the indicated entity. Detection
        is silent (no visual feedback) compared to  sim.handleProximitySensor .
        Also, the detectable flags of the entity are overridden if the entity is an
        object

        Args:
            sensorHandle (int): handle of the proximity sensor object
            entityHandle (int): handle of entity to detect (object or collection), or sim.handle_all to detect all detectable objects

        Returns:
            res (int): 0 (not detected) or 1 (detected)
            dist (float): distance from the sensor origin to the detected point. None/nil if result is different from 1
            point (list): position of the detected point relative to the sensor origin. None/nil if result is different from 1
            obj (int): handle of detected object. None/nil if result is different from 1
            n (list): normal vector of the surface where the point was detected. Normalized. Relative to the sensor reference frame. None/nil if result is different from 1

        """
        ...

    def checkProximitySensorEx(
        self,
        handle: int,
        entityHandle: int,
        detectionMode: int,
        detectionThreshold: float,
        maxAngle: float,
    ) -> Tuple[int, float, list, int, list]:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simCheckProximitySensorEx.htm
        Checks whether the proximity sensor detects the indicated entity. Detection
        is silent (no visual feedback) compared to  sim.handleProximitySensor .
        Also, the detectable flags of the entity are overridden if the entity is an
        object

        Args:
            handle (int): handle of the proximity sensor object
            entityHandle (int): handle of entity to detect (object or collection), or sim.handle_all to detect all detectable objects
            detectionMode (int): bit coded: bit0 (1) for front face detection, bit1 (2) for back face detection (bit0|bit1 needs to be true), bit2 (4) for fast detection (doesn't search for the closest point, just any point in the detection volume), bit3 (8) for limited angle detection (if set, maxAngle is taken into account).
            detectionThreshold (float): doesn't detect objects farther than detectionThreshold distance from sensor origin
            maxAngle (float): maximum detection angle (angle between detection ray and normal vector of the surface). Can be (0;pi/2). Only if bit3 of detectionMode is set will this parameter have an effect. Use this to realistically simulate ultrasonic sensors.

        Returns:
            res (int): 0 (not detected) or 1 (detected)
            dist (float): distance from the sensor origin to the detected point. None/nil if result is different from 1
            point (list): position of the detected point relative to the sensor origin. None/nil if result is different from 1
            object (int): handle of detected object. None/nil if result is different from 1
            n (list): normal vector of the surface where the point was detected. Normalized. Relative to the sensor reference frame. None/nil if result is different from 1

        """
        ...

    def checkProximitySensorEx2(
        self,
        sensorHandle: int,
        vertices: list,
        itemType: int,
        itemCount: int,
        mode: int,
        threshold: float,
        maxAngle: float,
    ) -> Tuple[int, float, list, list]:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simCheckProximitySensorEx2.htm
        Checks whether the proximity sensor detects the indicated points, segments
        or triangles. Detection is silent (no visual feedback)

        Args:
            sensorHandle (int): handle of the proximity sensor object
            vertices (list): an array containing vertices
            itemType (int): 0 for points, 1 for segments and 2 for triangles
            itemCount (int): the number of items that the 'vertices' array contains
            mode (int): bit coded: bit0 (1) for front face detection, bit1 (2) for back face detection (bit0|bit1 needs to be true), bit2 (4) for fast detection (doesn't search for the closest point, just any point in the detection volume), bit3 (8) for limited angle detection (if set, maxAngle is taken into account).
            threshold (float): doesn't detect objects farther than detectionThreshold distance from sensor origin
            maxAngle (float): maximum detection angle (angle between detection ray and normal vector of the surface). Can be (0;pi/2). Only if bit3 of detectionMode is set will this parameter have an effect. Use this to realistically simulate ultrasonic sensors

        Returns:
            res (int): 0 (not detected) or 1 (detected)
            dist (float): distance from the sensor origin to the detected point. None/nil if res is different from 1
            point (list): position of the detected point relative to the sensor origin. None/nil if res is different from 1
            n (list): normal vector of the surface where the point was detected. Normalized. Relative to the sensor reference frame. None/nil if res is different from 1

        """
        ...

    def checkVisionSensor(self, sensorHandle: int) -> Tuple[int, list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCheckVisionSensor.htm
        Checks whether the vision sensor detects the indicated entity. Detection is
        silent (no visual feedback) compared to  sim.handleVisionSensor . The
        vision callback functions  will be called on the acquired image. Also, the
        visibility state of the entity is overridden if the entity is an object

        Args:
            sensorHandle (int): handle of the vision sensor object

        Returns:
            result (int): 0 (no detection) or 1 (detection)
            auxPacket1 (list): packet of 15 auxiliary values: the minimum of intensity, red, green, blue, depth value, the maximum of intensity, red, green, blue, depth value, and the average of intensity, red, green, blue, depth value
            auxPacket2 (list): additional auxiliary value packet (e.g. from an image processing component)

        """
        ...

    def checkVisionSensorEx(
        self, sensorHandle: int, entityHandle: int, returnImage: bool
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCheckVisionSensorEx.htm
        Checks whether the vision sensor detects the indicated entity. Detection is
        silent (no visual feedback) compared to  sim.handleVisionSensor . The
        vision callback functions will be called on the acquired image. Also, the
        visibility state of the entity is overridden if the entity is an object

        Args:
            sensorHandle (int): handle of the vision sensor object. Can be combined with
            entityHandle (int): handle of entity to detect (object or collection), or sim.handle_all to detect all detectable objects
            returnImage (bool): specifies what should be returned. If true, the sensor's image buffer is returned, otherwise its depth buffer is returned

        Returns:
            buff (list): No detailed return description.

        """
        ...

    def closeScene(self) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCloseScene.htm Closes
        current scene, and switches to another open scene. If there is no other open
        scene, a new scene is then created. Can only be called from an  add-on , or
        from the sanbox script, when called from within CoppeliaSim

        Returns:
            result (int): the current scene index.

        """
        ...

    def computeMassAndInertia(self, shapeHandle: int, density: float) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simComputeMassAndInertia.htm
        Computes and applies the mass and inertia matrix for a shape, based on its
        convex representation. When calling this function while the simulation is
        running, one should then call sim.resetDynamicObject , for the changes to
        take effect

        Args:
            shapeHandle (int): handle of shape
            density (float): density expressed in kg/m^3

        Returns:
            result (int): 0 if the shape is not convex, otherwise 1

        """
        ...

    def copyPasteObjects(self, objectHandles: list, options: int) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCopyPasteObjects.htm
        Copies and pastes objects

        Args:
            objectHandles (list): array of object handles to copy and paste
            options (int): bit-coded:

        Returns:
            copiedObjectHandles (list): the duplicate object handles, where original and copy have the same location in their respective arrays (when script objects are stripped away, the array could contain -1 values)

        """
        ...

    def createCollection(self, options: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreateCollection.htm
        Creates a new  collection . A collection created in a simulation script , a
        customization script  or in the  main script  are automatically destroyed
        when the script ends

        Args:
            options (int): bit-coded options:

        Returns:
            collectionHandle (int): handle of the new collection

        """
        ...

    def createDummy(self, size: float) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreateDummy.htm Creates a
        dummy .

        Args:
            size (float): dummy size

        Returns:
            dummyHandle (int): No detailed return description.

        """
        ...

    def createForceSensor(
        self, options: int, intParams: list, floatParams: list
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreateForceSensor.htm
        Creates a  force sensor .

        Args:
            options (int): bit-coded options:
            intParams (list): 5 integer parameters (indexing (i) starts from 0 for Python and 1 for Lua):
            floatParams (list): 5 floating point parameters (indexing (i) starts from 0 for Python and 1 for Lua):

        Returns:
            sensorHandle (int): No detailed return description.

        """
        ...

    def createHeightfieldShape(
        self,
        options: int,
        shadingAngle: float,
        xPointCount: int,
        yPointCount: int,
        xSize: float,
        heights: list,
    ) -> int:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simCreateHeightfieldShape.htm
        Creates a heightfield  shape

        Args:
            options (int): bit-coded options:
            shadingAngle (float): shading angle
            xPointCount (int): number of rows and lines of the heightfield
            yPointCount (int): number of rows and lines of the heightfield.
            xSize (float): length of the x side of the heightfield
            heights (list): array of xPointCount*yPointCount height values

        Returns:
            objectHandle (int): handle of the newly created shape

        """
        ...

    def createJoint(
        self, jointType: int, jointMode: int, options: int, sizes: list
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreateJoint.htm Creates a
        joint

        Args:
            jointType (int): sim.joint_revolute
            jointMode (int): a
            options (int): reserved. Set to 0
            sizes (list): array of 2 values indicating the joint length and diameter. Can be None/nil for default values

        Returns:
            jointHandle (int): handle of the joint

        """
        ...

    def createOctree(
        self, voxelSize: float, options: int, pointSize: float
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreateOctree.htm Creates
        an empty  OC tree

        Args:
            voxelSize (float): size of the voxels
            options (int): bit-coded:
            pointSize (float): the size of the points in pixels, when voxels are rendered with points

        Returns:
            handle (int): handle of the OC tree

        """
        ...

    def createPath(
        self,
        ctrlPts: list,
        options: int,
        subdiv: int,
        smoothness: float,
        orientationMode: int,
        upVector: list,
    ) -> int:
        """
            URL: https://manual.coppeliarobotics.com/en/sim/simCreatePath.htm Creates a
            path .

            Args:
                ctrlPts (list): control points, specified in row-major order, with
        [x y z qx qy qz qw]
                options (int): bit-coded:
                subdiv (int): number of individual path points
                smoothness (float): value between 0.0 (linear interpolation) and 1.0 (100% Bezier interpolation)
                orientationMode (int): value specifiying how the individual path points are oriented along the path, if bit16 of options is set: 0: x along path, y is up, 1: x along path, z is up, 2: y along path, x is up, 3: y along path, z is up, 4: z along path, x is up, 5: z along path, y is up
                upVector (list): up vector, used for generating an extruded shape and for computing individual path point orientations

            Returns:
                pathHandle (int): No detailed return description.

        """
        ...

    def createPointCloud(
        self,
        maxVoxelSize: float,
        maxPtCntPerVoxel: int,
        options: int,
        pointSize: float,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreatePointCloud.htm
        Creates an empty  point cloud

        Args:
            maxVoxelSize (float): maximum size of the OC tree voxels containing points
            maxPtCntPerVoxel (int): maximum number of points allowed in a same OC tree voxel
            options (int): bit-coded:
            pointSize (float): size of the points, in pixels

        Returns:
            handle (int): handle of the point cloud

        """
        ...

    def createPrimitiveShape(
        self, primitiveType: int, sizes: list, options: int
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreatePrimitiveShape.htm
        Creates a primitive shape

        Args:
            primitiveType (int): the
            sizes (list): 3 values indicating the size of the shape
            options (int): Bit-coded:

        Returns:
            shapeHandle (int): handle of the newly created shape

        """
        ...

    def createProximitySensor(
        self,
        sensorType: int,
        subType: int,
        options: int,
        intParams: list,
        floatParams: list,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreateProximitySensor.htm
        Creates a  proximity sensor

        Args:
            sensorType (int): desired
            subType (int): deprecated. Set to 16
            options (int): bit-coded options:
            intParams (list): 8 integer parameters (indexing (i) starts from 0 for Python and 1 for Lua):
            floatParams (list): 15 floating point parameters (indexing (i) starts from 0 for Python and 1 for Lua):

        Returns:
            sensorHandle (int): No detailed return description.

        """
        ...

    def createScript(
        self, scriptType: int, scriptText: str, options: int
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreateScript.htm Creates
        a  script object .

        Args:
            scriptType (int): the
            scriptText (str): the content of the script
            options (int): bit-coded options:

        Returns:
            scriptHandle (int): No detailed return description.

        """
        ...

    def createTexture(
        self,
        fileName: str,
        options: int,
        planeSizes: list,
        scalingUV: list,
        xy_g: list,
        fixedResolution: int,
        resolution: list,
    ) -> Tuple[int, int, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreateTexture.htm Creates
        a planar shape, that will be textured with a new, or imported texture

        Args:
            fileName (str): filename of the texure to import, or an empty str if you wish to create a new texture.
            options (int): bit-coded:
            planeSizes (list): array of 2 values: the dimensions of the planar shape that will be generated. Can be None/nil for default dimensions.
            scalingUV (list): array of 2 values: the desired scaling of the texture, along the U and V directions. Can be None/nil for default scalings.
            xy_g (list): array of 3 values: the texture x/y shift, and the texture gamma-rotation. Can be None/nil for default shift/rotation values.
            fixedResolution (int): 0 to import the shape with its original resolution. Otherwise, specify a power of 2 value which will be the maximum texture resolution (the texture will also be applied a power of 2 resolution).
            resolution (list): Description not provided

        Returns:
            shape (int): handle of the created planar shape
            id (int): new texture ID. If a same texture is already present, the old texture ID will be returned
            res (list): the effective texture resolution

        """
        ...

    def createVisionSensor(
        self, options: int, intParams: list, floatParams: list
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simCreateVisionSensor.htm
        Creates a  vision sensor .

        Args:
            options (int): bit-coded options:
            intParams (list): 4 integer parameters (indexing (i) starts from 0 for Python and 1 for Lua):
            floatParams (list): 11 floating point parameters (indexing (i) starts from 0 for Python and 1 for Lua):

        Returns:
            sensorHandle (int): No detailed return description.

        """
        ...

    def destroyCollection(self, collectionHandle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simDestroyCollection.htm
        Removes a  collection

        Args:
            collectionHandle (int): handle of the collection to remove

        """
        ...

    def destroyGraphCurve(self, graphHandle: int, curveId: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simDestroyGraphCurve.htm
        Destroys a graph stream or curve

        Args:
            graphHandle (int): handle of the graph
            curveId (int): id of the stream or curve, -1 to remove all streams/curves

        """
        ...

    def duplicateGraphCurveToStatic(
        self, graphHandle: int, curveId: int, staticCurveName: str
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simDuplicateGraphCurveToStat
        ic.htm Duplicates a graph stream or curve, and freezes it

        Args:
            graphHandle (int): handle of the graph
            curveId (int): id of the stream or curve
            staticCurveName (str): name of the new static stream/curve

        Returns:
            staticCurveId (int): id of the created static stream or curve

        """
        ...

    def executeScriptstr(
        self, strToExecute: str, scriptHandle: int
    ) -> Tuple[int, Any]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simExecuteScriptstr.htm
        Executes some code in a specific script (from a  plugin , the main client
        application , or from another script). The target script must be initialized
        for this call to succeed, e.g. when calling simulation scripts , then
        simulation must be running From C/C++, data exchange between a plugin and a
        script happens via a  stack . Reading and writing arguments from/to the
        stack gives you a maximum of flexibility, and you wil be able to exchange
        also complex data structures. But it can also be tedious and error prone.
        Use instead the helper classes located in  programming/include/simStack

        Args:
            strToExecute (str): a str representing the code to execute in the specified script. An optional @python or @lua can be appended, to force a specific language
            scriptHandle (int): handle of the script, or sim.handle_self to target the script itself.

        Returns:
            result (int): 0 or 1
            executionResult (Any): return value of the executed code

        """
        ...

    def floatingViewAdd(
        self,
        posX: float,
        posY: float,
        sizeX: float,
        sizeY: float,
        options: int,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simFloatingViewAdd.htm Adds
        a floating view to current page

        Args:
            posX (float): Description not provided
            posY (float): relative position of the center of the floating view. Accepted values are between 0.0 and 1.0
            sizeX (float): Description not provided
            sizeY (float): relative size of the floating view. Accepted values are between 0.0 and 1.0
            options (int): bit-coded:

        Returns:
            floatingViewHandle (int): handle of the floating view

        """
        ...

    def floatingViewRemove(self, floatingViewHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simFloatingViewRemove.htm
        Removes a floating view previously added with  sim.floatingViewAdd .

        Args:
            floatingViewHandle (int): handle of the floating view to be removed

        Returns:
            result (int): No detailed return description.

        """
        ...

    def generateTextShape(
        self,
        txt: str,
        color: list,
        height: float,
        centered: bool,
        alphabetLocation: str,
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGenerateTextShape.htm
        Generates a 3D text model.

        Args:
            txt (str): the text str
            color (list): the text color. Optional
            height (float): the height of the text. Optional
            centered (bool): whether the text should be centered. Optional
            alphabetLocation (str): the path to an alphabet model. Optional

        Returns:
            modelHandle (int): No detailed return description.

        """
        ...

    def generateTimeOptimalTrajectory(
        self,
        path: list,
        pathLengths: list,
        minMaxVel: list,
        minMaxAccel: list,
        trajPtSamples: int,
        boundaryCondition: str,
        timeout: float,
        calculationScriptHandle: int,
    ) -> Tuple[list, list, int]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGenerateTimeOptimalTrajec
        tory.htm Generates a time optimal trajectory, based on the TOPPRA library

        Args:
            path (list): path, specified in row-major order, e.g. a path containing two 3D positions would be [x1 y1 z1 x2 y2 z2]
            pathLengths (list): lengths of a path. Each path point should have a corresponding length value (as the distance from the path's first point, along the path). See also
            minMaxVel (list): minimum and maximum allowed velocity, for each dimension/axis, e.g. {xmin,xmax,ymin,ymax,zmin,zmax}
            minMaxAccel (list): minimum and maximum allowed acceleration, for each dimension/axis, e.g. [xmin xmax ymin ymax zmin zmax]
            trajPtSamples (int): desired number of path points/configurations
            boundaryCondition (str): boundary condition
            timeout (float): a timeout duration
            calculationScriptHandle (int): optional. Can indicate a script handle returned in a previous call to this function, including -1 to indicate that the created calculation script should be returned for future reuse

        Returns:
            outP (list): generated path points
            times (list): generated times corresponding to path points
            scriptHandle (int): the handle of the calculation script for reuse in a subsequent call to this function

        """
        ...

    def getApiFunc(self, scriptHandle: int, apiWord: str) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetApiFunc.htm Retrieves
        all API functions and variables that match a specific word. Useful for
        script code auto-completion functionality

        Args:
            scriptHandle (int): Description not provided
            apiWord (str): word that API functions and variables should match, e.g. "sim.getObj". Only matches up to the first dot are returned, if the apiWord does not contain any dot. To retrieve all functions and variables, leave apiWord empty. To retrieve only functions, add '+' as prefix. To retrieve only variables, add '-' as prefix.

        Returns:
            funcsAndVars (list): array containing all matching API functions and variables.

        """
        ...

    def getApiInfo(self, scriptHandle: int, apiWord: str) -> str:
        """
            URL: https://manual.coppeliarobotics.com/en/sim/simGetApiInfo.htm Returns
            the call tip (or info text) for an API function

            Args:
                scriptHandle (int): handle of the script
        . Can be -1 to be script agnostic
                apiWord (str): API functions or variable to retrieve the info for, e.g. "sim.getObject"

            Returns:
                info (str): information related to the API function or variable

        """
        ...

    def getBoolProperty(
        self, target: int, propertyName: str, options: dict
    ) -> bool:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetBoolProperty.htm
        Fetches a boolean property

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (bool): property value

        """
        ...

    def getBufferProperty(
        self, target: int, propertyName: str, options: dict
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetBufferProperty.htm
        Fetches a buffer property

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (bytes): property value

        """
        ...

    def getClosestPosOnPath(
        self, path: list, pathLengths: list, absPt: list
    ) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetClosestPosOnPath.htm
        Returns the position or distance along a path that is closest to a specified
        point in space

        Args:
            path (list): path, specified in row-major order, with x/y/z values for each path point
            pathLengths (list): lengths of a path. Each path point should have a corresponding length value (as the distance from the path's first point, along the path). See alsoï¿½
            absPt (list): point in 3D space

        Returns:
            posAlongPath (float): position/distance along the path

        """
        ...

    def getCollectionObjects(self, collectionHandle: int) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetCollectionObjects.htm
        Retrieves the object handles that compose a  collection

        Args:
            collectionHandle (int): handle of the collection

        Returns:
            objectHandles (list): array of n object handles

        """
        ...

    def getColorProperty(
        self, target: int, propertyName: str, options: dict
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetColorProperty.htm
        Fetches a color property (float[3])

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (list): property value

        """
        ...

    def getConfigDistance(
        self, configA: list, configB: list, metric: list, types: list
    ) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetConfigDistance.htm
        Returns the distance between two configurations points

        Args:
            configA (list): the first configuration, e.g. in case of a 3D pose (position+quaternion), would be [x1 y1 z1 qx1 qy1 qz1 qw1]
            configB (list): the second configuration
            metric (list): an optional array specifying the metric to use to compute distances. e.g. if the specified configurations were 3D positions, the distance between two configurations would be calculated as SQRT( mx * (x2 - x1)^2 + my * (y2 - y1)^2 + mz * (z2 - z1)^2 ), where [mx my mz] would be the metric.
            types (list): an optional array specifying the type of each configuration value/dimension: 0=cartesian value, 1=2pi-cyclic value, 2=quaternion value. e.g. a configuration representing 3D poses should use a types argument [0 0 0 2 2 2 2], a configuration representing revolute and cyclic joints should use a types argument [1 1 1 ...]

        Returns:
            distance (float): the distance between the two configurations

        """
        ...

    def getContactInfo(
        self, dynamicPass: int, objectHandle: int, index: int
    ) -> Tuple[list, list, list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetContactInfo.htm
        Retrieves contact point information of a dynamic simulation pass.

        Args:
            dynamicPass (int): a specific dynamic sub-step index or sim.handle_all. By default a call to
            objectHandle (int): handle of a specific object you wish to retrieve contacts from, or sim.handle_all to retrieve all contacts in the scene.
            index (int): zero-based index of the contact to retrieve

        Returns:
            coll (list): handles of the two objects contacting. The handles might also refer to particle objects that are not treated as regular scene objects
            point (list): coordinates of the contact
            rForce (list): vector that represents the force generated by the contact
            n (list): Description not provided

        """
        ...

    def getEulerAnglesFromMatrix(self, matrix: list) -> list:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simGetEulerAnglesFromMatrix.htm
        Retrieves the  Euler angles  from a transformation matrix

        Args:
            matrix (list): array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]

        Returns:
            eulerAngles (list): array of 3 values

        """
        ...

    def getExplicitHandling(self, objectHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetExplicitHandling.htm
        Retrieves the explicit handling flags for a scene object

        Args:
            objectHandle (int): handle of a scene object

        Returns:
            explicitHandlingFlags (int): the explicit handling flags for the specified object (for now only bit 0 is used)

        """
        ...

    def getExtensionstr(self, objectHandle: int, index: int, key: str) -> str:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetExtensionstr.htm
        Retrieves a str that describes additional environment or object
        properties, mainly used by extension plugins.

        Args:
            objectHandle (int): handle of an object, or -1 if you wish to retrieve the extension str of the environment
            index (int): keep to -1, unless the object is a shape, and you wish to retrieve the extension str of a shape component (since a shape can be a compound of several other shapes)
            key (str): optional key indicating what value to retrieve. If None/nil is specified, then the whole extension str is returned. Keys should have the form of

        Returns:
            thestr (str): No detailed return description.

        """
        ...

    def getFloatArrayProperty(
        self, target: int, propertyName: str, options: dict
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetFloatArrayProperty.htm
        Fetches a float array property (double[])

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (list): property value

        """
        ...

    def getFloatProperty(
        self, target: int, propertyName: str, options: dict
    ) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetFloatProperty.htm
        Fetches a float property (double)

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (float): property value

        """
        ...

    def getGenesisEvents(self) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetGenesisEvents.htm
        Retrieves all events that allow to reconstruct a scene's (mostly) visual
        content remotely

        Returns:
            events (bytes): No detailed return description.

        """
        ...

    def getIntArray2Property(
        self, target: int, propertyName: str, options: dict
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetIntArray2Property.htm
        Fetches an int[2] property

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (list): property value

        """
        ...

    def getIntArrayProperty(
        self, target: int, propertyName: str, options: dict
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetIntArrayProperty.htm
        Fetches an int array property (int[])

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (list): property value

        """
        ...

    def getIntProperty(
        self, target: int, propertyName: str, options: dict
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetIntProperty.htm
        Fetches an int32 property

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (int): property value

        """
        ...

    def getJointDependency(self, jointHandle: int) -> Tuple[int, float, float]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetJointDependency.htm
        Retrieves joint dependency information, when the joint is in dependent mode

        Args:
            jointHandle (int): handle of the slave joint

        Returns:
            masterJointHandle (int): handle of the master joint, or -1 if the joint is not dependent
            offset (float): offset in equation slave = offset + master * multCoeff
            multCoeff (float): coeff in equation slave = offset + master * multCoeff

        """
        ...

    def getJointForce(self, jointHandle: int) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetJointForce.htm
        Retrieves the force or torque applied to a joint along/about its active
        axis. This function retrieves meaningful information only if the joint is
        prismatic or revolute, and is dynamically enabled. With the Bullet, MuJoCo
        and Newton engine, this function returns the force or torque applied to the
        joint motor  (torques from joint limits are not taken into account). With
        the ODE and Vortex engine, this function returns the total force or torque
        applied to a joint along/about its z-axis

        Args:
            jointHandle (int): handle of the joint. Can be combined with

        Returns:
            forceOrTorque (float): force or the torque applied to the joint along/about its z-axis.

        """
        ...

    def getJointInterval(self, objectHandle: int) -> Tuple[bool, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetJointInterval.htm
        Retrieves the interval parameters of a joint

        Args:
            objectHandle (int): handle of the joint

        Returns:
            cyclic (bool): indicates whether the joint is cyclic (the joint varies between -pi and +pi in a cyclic manner).
            interval (list): interval of the joint. interval[1] is the joint minimum allowed value, interval[2] is the joint range (the maximum allowed value is interval[1]+interval[2]). When the joint is "cyclic", then the interval parameters don't have any meaning.

        """
        ...

    def getJointMode(self, jointHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetJointMode.htm
        Retrieves the operation mode of a joint

        Args:
            jointHandle (int): handle of the joint object

        Returns:
            jointMode (int): the

        """
        ...

    def getJointPosition(self, objectHandle: int) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetJointPosition.htm
        Retrieves the linear/angular position of a joint. This function cannot be
        used with spherical joints (use  sim.getObjectChildPose  instead)

        Args:
            objectHandle (int): handle of the joint

        Returns:
            position (float): linear/angular position of the joint

        """
        ...

    def getJointTargetForce(self, jointHandle: int) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetJointTargetForce.htm
        Retrieves the force or torque that a joint can exert

        Args:
            jointHandle (int): handle of the joint

        Returns:
            forceOrTorque (float): the maximum force or torque the joint can apply. The sign indicates the desired movement direction

        """
        ...

    def getJointTargetPosition(self, objectHandle: int) -> float:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simGetJointTargetPosition.htm
        Retrieves the target linear/angular position of a joint

        Args:
            objectHandle (int): handle of the joint object

        Returns:
            targetPosition (float): target position of the joint

        """
        ...

    def getJointTargetVelocity(self, objectHandle: int) -> float:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simGetJointTargetVelocity.htm
        Retrieves the target linear/angular velocity of a non-spherical joint

        Args:
            objectHandle (int): handle of the joint object

        Returns:
            targetVelocity (float): target velocity of the joint.

        """
        ...

    def getJointType(self, objectHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetJointType.htm
        Retrieves the type of a joint

        Args:
            objectHandle (int): handle of the joint

        Returns:
            jointType (int): type of the joint:

        """
        ...

    def getJointVelocity(self, jointHandle: int) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetJointVelocity.htm
        Retrieves the linear or angular velocity of a joint. The velocity is a
        measured velocity (i.e. from one simulation step to the next), and is
        available for all joints in the scene

        Args:
            jointHandle (int): handle of a joint

        Returns:
            velocity (float): No detailed return description.

        """
        ...

    def getLastInfo(self) -> str:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetLastInfo.htm Retrieves
        and clears the information str generated by last API call

        Returns:
            info (str): No detailed return description.

        """
        ...

    def getLinkDummy(self, dummyHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetLinkDummy.htm
        Retrieves the object handle of the dummy linked to this one

        Args:
            dummyHandle (int): handle of the dummy whose linked dummy has to be retrieved

        Returns:
            linkedDummyHandle (int): handle of the dummy linked to the specified dummy object, or -1 if the dummy is not linked

        """
        ...

    def getLongProperty(
        self, target: int, propertyName: str, options: dict
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetLongProperty.htm
        Fetches an int64 property

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (int): property value

        """
        ...

    def getMatrixInverse(self, matrix: list) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetMatrixInverse.htm
        Inverts a transformation matrix

        Args:
            matrix (list): the input matrix

        Returns:
            matrix (list): the output matrix

        """
        ...

    def getNavigationMode(self) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetNavigationMode.htm
        Retrieves the navigation and selection mode for the mouse

        Returns:
            navigationMode (int): navigation mode

        """
        ...

    def getObject(self, objectPath: str, options: dict = {}) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObject.htm Retrieves
        an object handle based on its path and alias

        Args:
            objectPath (str): path and alias of the object to find. See the section on
            options (dict): optional map indicating how the object should be searched:

        Returns:
            objectHandle (int): handle of object or -1

        """
        ...

    def getObjectAlias(self, objectHandle: int, options: int) -> str:
        """
            URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectAlias.htm
            Retrieves the alias or path of an object based on its handle

            Args:
                objectHandle (int): handle of the object.
                options (int): alias formating options:


        -1: naked alias (e.g. "alias")

            Returns:
                alias (str): alias or path of the object

        """
        ...

    def getObjectChild(self, objectHandle: int, index: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectChild.htm
        Retrieves the handle of an object's child object

        Args:
            objectHandle (int): handle of the object, or sim.handle_scene to retrieve orphan objects
            index (int): zero-based index of the child's position. To retrieve all children of an object, call the function by increasing the index until the return value is -1

        Returns:
            childHandle (int): handle of child object or -1 if the child doesn't exist at that index

        """
        ...

    def getObjectChildPose(self, objectHandle: int) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectChildPose.htm
        Retrieves the intrinsic or internal transformation of an object. For a
        joint, this is the transformation caused by the joint movement, mainly. For
        joints and force sensors, this will also include a possible error
        transformation caused by the physics engine (a physics engine can cause
        joints and force sensors to come apart, when constraints can't be perfectly
        resolved)

        Args:
            objectHandle (int): handle of the joint

        Returns:
            pose (list): the pose

        """
        ...

    def getObjectColor(
        self, objectHandle: int, index: int, colorComponent: int
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectColor.htm
        Retrieves the color of a scene object

        Args:
            objectHandle (int): handle of the object
            index (int): zero-based index of the color, if the object has several colors
            colorComponent (int): color component

        Returns:
            rgbData (list): red, green and blue components of the color (3 values)

        """
        ...

    def getObjectFromUid(self, objectUid: int, options: dict) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectFromUid.htm
        Retrieves an object handle based on its unique identifier

        Args:
            objectUid (int): the object unique identifier.
            options (dict): optional map indicating how the object should be searched. {

        Returns:
            objectHandle (int): handle of object

        """
        ...

    def getObjectHierarchyOrder(self, objectHandle: int) -> Tuple[int, int]:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simGetObjectHierarchyOrder.htm
        Retrieves the zero-based position of an object among its siblings in the
        scene hierarchy

        Args:
            objectHandle (int): the handle of the object

        Returns:
            order (int): the position of the object
            totalSiblingsCount (int): Description not provided

        """
        ...

    def getObjectMatrix(
        self, objectHandle: int, relativeToObjectHandle: int
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectMatrix.htm
        Retrieves the transformation matrix of an object

        Args:
            objectHandle (int): handle of the object. Can be combined with sim.handleflag_reljointbaseframe (see next argument)
            relativeToObjectHandle (int): indicates relative to which reference frame we want the matrix. Specify sim.handle_world to retrieve the absolute transformation matrix, sim.handle_inverse to retrieve the inverse of the absolute transformation matrix, sim.handle_parent to retrieve the transformation matrix relative to the object's parent, or an object handle relative to whose reference frame we want the transformation matrix. If this handle is the handle of a joint, then the matrix relative to the joint's moving frame will be returned (unless

        Returns:
            matrix (list): array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]

        """
        ...

    def getObjectOrientation(
        self, objectHandle: int, relativeToObjectHandle: int
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectOrientation.htm
        Retrieves the orientation ( Euler angles ) of an object

        Args:
            objectHandle (int): handle of the object. Can be combined with sim.handleflag_reljointbaseframe (see next argument)
            relativeToObjectHandle (int): indicates relative to which reference frame we want the orientation. Specify sim.handle_world to retrieve the absolute orientation, sim.handle_parent to retrieve the orientation relative to the object's parent, or an object handle relative to whose reference frame you want the orientation. If this handle is the handle of a joint, then the orientation relative to the joint's moving frame will be returned (unless

        Returns:
            eulerAngles (list): Euler angles [alpha beta gamma]

        """
        ...

    def getObjectParent(self, objectHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectParent.htm
        Retrieves the handle of an object's parent object

        Args:
            objectHandle (int): handle of the object

        Returns:
            parentHandle (int): handle of parent or -1 if the parent doesn't exist

        """
        ...

    def getObjectPose(
        self, objectHandle: int, relativeToObjectHandle: int
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectPose.htm
        Retrieves the pose of an object

        Args:
            objectHandle (int): handle of the object. Combine with sim.handleflag_wxyzquat to retrieve the quaternion as [qw qx qy qz] order instead of [qx qy qz qw] order. Can also be combined with sim.handleflag_reljointbaseframe (see next argument)
            relativeToObjectHandle (int): indicates relative to which reference frame we want the pose. Specify sim.handle_world to retrieve the absolute pose, sim.handle_inverse to retrieve the inverse of the absolute pose, sim.handle_parent to retrieve the pose relative to the object's parent, or an object handle relative to whose reference frame we want the pose. If this handle is the handle of a joint, then the pose relative to the joint's moving frame will be returned (unless

        Returns:
            pose (list): pose array: [x y z qx qy qz qw]

        """
        ...

    def getObjectPosition(
        self, objectHandle: int, relativeToObjectHandle: int
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectPosition.htm
        Retrieves the position of an object

        Args:
            objectHandle (int): handle of the object. Can be combined with sim.handleflag_reljointbaseframe (see next argument)
            relativeToObjectHandle (int): indicates relative to which reference frame we want the position. Specify sim.handle_world to retrieve the absolute position, sim.handle_parent to retrieve the position relative to the object's parent, or an object handle relative to whose reference frame we want the position. If this handle is the handle of a joint, then the position relative to the joint's moving frame will be returned (unless

        Returns:
            position (list): array of 3 values [x y z]

        """
        ...

    def getObjectQuaternion(
        self, objectHandle: int, relativeToObjectHandle: int
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectQuaternion.htm
        Retrieves the quaternion of an object

        Args:
            objectHandle (int): handle of the object. Combine with sim.handleflag_wxyzquat to retrieve the quaternion as [qw qx qy qz] order instead of [qx qy qz qw] order. Can also be combined with sim.handleflag_reljointbaseframe (see next argument)
            relativeToObjectHandle (int): indicates relative to which reference frame we want the orientation. Specify sim.handle_world to retrieve the absolute orientation, sim.handle_parent to retrieve the orientation relative to the object's parent, or an object handle relative to whose reference frame you want the orientation. If this handle is the handle of a joint, then the quaternion relative to the joint's moving frame will be returned (unless

        Returns:
            quaternion (list): the quaternion [qx qy qz qw]

        """
        ...

    def getObjects(self, index: int, objectType: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjects.htm Retrieves
        object handles. Use this in a loop where index starts at 0 and is
        incremented to get all object handles in the scene

        Args:
            index (int): object index. First object is located at index 0
            objectType (int): object type (sim.sceneobject_shape, sim.sceneobject_joint, etc. (see the

        Returns:
            objectHandle (int): handle of the object or -1 if no object is located at that index

        """
        ...

    def getObjectSel(self) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectSel.htm
        Retrieves the handles of selected objects

        Returns:
            selectedObjects (list): the handles of selected objects

        """
        ...

    def getObjectsInTree(
        self, treeBaseHandle: int, objectType: int, options: int
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectsInTree.htm
        Retrieves object handles in a given hierarchy tree

        Args:
            treeBaseHandle (int): handle of the object that describes the hierarchy tree, or sim.handle_scene for all objects in the scene.
            objectType (int): object type
            options (int): bit-coded:

        Returns:
            objects (list): an array containing object handles

        """
        ...

    def getObjectSizeFactor(self, objectHandle: int) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectSizeFactor.htm
        Retrieves the size factor of a scene object. The size factor is different
        from the real object size. Use this to be able to adapt to scaling
        operations

        Args:
            objectHandle (int): handle of the scene object

        Returns:
            sizeFactor (float): No detailed return description.

        """
        ...

    def getObjectType(self, objectHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectType.htm
        Retrieves the type of an object

        Args:
            objectHandle (int): handle of the object

        Returns:
            objectType (int): type of the object (sim.sceneobject_shape, sim.sceneobject_joint, etc. (see the

        """
        ...

    def getObjectUid(self, objectHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectUid.htm
        Retrieves the unique identifier of an object: throughout a CoppeliaSim
        session, there won't be two identical unique identifiers. Unique identifiers
        are however not persistent (i.e. are not saved with the object)

        Args:
            objectHandle (int): object handle

        Returns:
            uid (int): the unique identifier

        """
        ...

    def getObjectVelocity(self, objectHandle: int) -> Tuple[list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetObjectVelocity.htm
        Retrieves the linear and/or angular velocity of an object, in absolute
        coordinates. The velocity is a measured velocity (i.e. from one simulation
        step to the next), and is available for all objects in the scene

        Args:
            objectHandle (int): handle of a

        Returns:
            linearVelocity (list): array of 3 values that represent the linear velocity
            angularVelocity (list): array of 3 values that represent the angular velocity

        """
        ...

    def getOctreeVoxels(self, octreeHandle: int) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetOctreeVoxels.htm
        Retrieves voxel positions from an  OC tree

        Args:
            octreeHandle (int): handle of the OC tree

        Returns:
            voxels (list): the voxel [x y z] positions, relative to the OC tree reference frame

        """
        ...

    def getPage(self) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPage.htm Retrieves the
        current page index (view)

        Returns:
            pageIndex (int): page index

        """
        ...

    def getPathInterpolatedConfig(
        self,
        path: list,
        pathLengths: list,
        t: float,
        method: dict = {"type": "linear", "strength": 1.0, "forceOpen": False},
        types: list[int] | None= None,
    ) -> list:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simGetPathInterpolatedConfig.htm
        Returns an interpolated configuration from a path

        Args:
            path (list): the path, specified in row-major order, e.g. a path containing two 3D poses (position+quaternion) would be [x1 y1 z1 qx1 qy1 qz1 qw1 x2 y2 z2 qx2 qy2 qz2 qw2]
            pathLengths (list): the lengths of a path. Each path point should have a corresponding length value (as the distance from the path's first point, along the path). See also
            t (float): the distance from the beginning of the path, where the interpolation point should be picked from
            method (dict): an optional map specifying the type of interpolation (linear or quadraticBezier), whether the path should be considered as open, even if the first and last path points overlap, and the bezier strength (0.05-1.0)
            'strength': 1.0 (Any): Description not provided
            'forceOpen': False} (Any): Description not provided
            types (list[int] | None): an optional array specifying the type of each configuration value/dimension: 0=cartesian value, 1=2pi-cyclic value, 2=quaternion value. e.g. a configuration representing 3D poses should use a types argument [0 0 0 2 2 2 2], a configuration representing revolute and cyclic joints should use a types argument [1 1 1 ...]

        Returns:
            config (list): the interpolated path configuration

        """
        ...

    def getPathLengths(
        self, path: list, dof: int, distCallback: str
    ) -> Tuple[list, float]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPathLengths.htm
        Returns the lengths of a path in 1, 2 or 3D Cartesian space, even if more
        coordinates are provided. Each path point will have a corresponding length
        value (taken as the distance from the path's first point, along the path)

        Args:
            path (list): the path, specified in row-major order, e.g. a path containing two 3D poses (position+quaternion) would be [x1 y1 z1 qx1 qy1 qz1 qw1 x2 y2 z2 qx2 qy2 qz2 qw2]
            dof (int): the size or dimension of path points, e.g. in case of a 3D pose, this would be 7 (however only the first 3 dimensions would be taken into account)
            distCallback (str): an optional function that takes as input two configurations, and returns the calculated distance between them. See also

        Returns:
            pathLengths (list): the lengths corresponding to each path point
            totalLength (float): the total length of the path

        """
        ...

    def getPluginInfo(self, pluginName: str, infoType: int) -> Any:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPluginInfo.htm Returns
        auxiliary information about a loaded plugin

        Args:
            pluginName (str): name of the plugin. See
            infoType (int): type of information

        Returns:
            str/int info (Any): No detailed return description.

        """
        ...

    def getPluginName(self, index: int) -> str:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPluginName.htm
        Retrieves a plugin name based on an index

        Args:
            index (int): index to a plugin. To list-up all plugin names, start with index=0 and increment index until return value is None/nil

        Returns:
            pluginName (str): No detailed return description.

        """
        ...

    def getPointCloudOptions(
        self, pcHandle: int
    ) -> Tuple[float, int, int, float]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPointCloudOptions.htm
        Gets various properties of a  point cloud

        Args:
            pcHandle (int): handle of the point cloud

        Returns:
            maxVoxelS (float): maximum size of the OC tree voxels containing points
            maxPtCntPerVoxel (int): maximum number of points allowed in a same OC tree voxel
            opt (int): bit-coded:
            ps (float): size of the points, in pixels

        """
        ...

    def getPointCloudPoints(self, pointCloudHandle: int) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPointCloudPoints.htm
        Retrieves point positions from a  point cloud

        Args:
            pointCloudHandle (int): handle of the point cloud

        Returns:
            points (list): the point [x y z] positions, relative to the point cloud reference frame

        """
        ...

    def getPoseInverse(self, pose: list) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPoseInverse.htm
        Inverts a pose

        Args:
            pose (list): the input pose

        Returns:
            pose (list): the output pose

        """
        ...

    def getPoseProperty(
        self, target: int, propertyName: str, options: dict
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPoseProperty.htm
        Fetches a pose property (double[7]: x, y, z, qx, qy, qz, qw)

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (list): property value

        """
        ...

    def getProperties(self, target: int, options: dict) -> dict:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetProperties.htm
        Convenience function to fetches all properties of a specific target item

        Args:
            target (int): target item
            options (dict): an optional map. Set options.skipLarge = true to skip large data

        Returns:
            properties (dict): properties

        """
        ...

    def getPropertiesInfos(self, target: int, options: dict) -> dict:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPropertiesInfos.htm
        Convenience function to fetches all properties infos of a specific target
        item

        Args:
            target (int): target item
            options (dict): an optional map

        Returns:
            propertiesInfo (dict): properties infos

        """
        ...

    def getProperty(
        self, target: int, propertyName: str, options: dict
    ) -> Any:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetProperty.htm
        Convenience functon to fetch a property

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (any): property value

        """
        ...

    def getPropertyInfo(
        self, target: int, propertyName: str
    ) -> Tuple[int, int, str]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPropertyInfo.htm
        Fetches information about a specific property

        Args:
            target (int): target item
            propertyName (str): property name

        Returns:
            type (int): property type
            flags (int): property flags
            description (str): property description

        """
        ...

    def getPropertyName(self, target: int, index: int, options: dict) -> str:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetPropertyName.htm
        Fetches the name of a property, based on an index

        Args:
            target (int): target item
            index (int): property index
            options (dict): an optional map. Set options.prefix to perform an initial filtering based on a prefix

        Returns:
            propertyName (str): property name

        """
        ...

    def getQuaternionProperty(
        self, target: int, propertyName: str, options: dict
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetQuaternionProperty.htm
        Fetches a quaternion property (double[4]: qx, qy, qz, qw)

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (list): property value

        """
        ...

    def getRandom(self, seed: int) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetRandom.htm Generates a
        random value in the range between 0.0 and 1.0. The value is generated from
        an individual generator attached to the calling script

        Args:
            seed (int): an optional number that can be used to seed/reseed the random number generator. Leave empty or set to None/nil if the generator should not be reseeded.

        Returns:
            randomValue (float): No detailed return description.

        """
        ...

    def getRealTimeSimulation(self) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetRealTimeSimulation.htm
        Indicates whether the simulation is real-time

        Returns:
            result (int): No detailed return description.

        """
        ...

    def getReferencedHandles(self, objectHandle: int, tag: str) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetReferencedHandles.htm
        Retrieves a list of custom handles, linking a given scene object to other
        scene objects

        Args:
            objectHandle (int): handle of the scene object that stores the list of handles. Can be optionally combined with
            tag (str): a tag: only handles stored within that tag are retrieved. defaults to an empty tag

        Returns:
            referencedHandles (list): an array with scene object handles

        """
        ...

    def getReferencedHandlesTags(self, objectHandle: int) -> list:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simGetReferencedHandlesTags.htm
        Retrieves a list of all referenced handles tags

        Args:
            objectHandle (int): handle of the scene object that stores the list of handles. Can be optionally combined with

        Returns:
            tags (list): an array with found tags

        """
        ...

    def getRotationAxis(
        self, poseStart: list, poseGoal: list
    ) -> Tuple[list, float]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetRotationAxis.htm
        Retrieves an axis and rotation angle that brings one pose or transformation
        matrix onto another one. The translation part of the poses/matrices is
        ignored. This function, when used in combination with  sim.rotateAroundAxis
        , can be used to build interpolations between transformation matrices

        Args:
            poseStart (list): Description not provided
            poseGoal (list): Description not provided

        Returns:
            axis (list): the rotation axis in absolute coordinates [Vx Vy Vz]
            angle (float): the rotation angle

        """
        ...

    def getScaledImage(
        self,
        imageIn: bytes,
        resolutionIn: list,
        desiredResolutionOut: list,
        options: int,
    ) -> Tuple[bytes, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetScaledImage.htm
        Generates a scaled-up or scaled down version of the input image

        Args:
            imageIn (bytes): image buffer (rgb or rgba values)
            resolutionIn (list): resolution of the input image
            desiredResolutionOut (list): Description not provided
            options (int): bit-coded:

        Returns:
            imageOut (bytes): buffer containing the output image data
            effectiveRolutionOut (list): Description not provided

        """
        ...

    def getScript(self, scriptType: int, scriptName: str) -> int:
        """
            URL: https://manual.coppeliarobotics.com/en/sim/simGetScript.htm Retrieves
            the handle of a script. For script objects, use sim.getObject instead

            Args:
                scriptType (int): type of the script
        , or sim.handle_self
                scriptName (str): name of the add-on, in case of an add-on

            Returns:
                scriptHandle (int): No detailed return description.

        """
        ...

    def getScriptFunctions(self, scriptHandle: int) -> map:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetScriptFunctions.htm
        Retrieves a map of another script functions, that can be called

        Args:
            scriptHandle (int): the handle of the script. See

        Returns:
            object (map): a meta object. Functions can be called with object:functionName()

        """
        ...

    def getShapeBB(self, shapeHandle: int) -> Tuple[list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetShapeBB.htm Returns
        the size and relative pose of a shape's bounding box

        Args:
            shapeHandle (int): handle of the shape

        Returns:
            size (list): size array [Sx Sy Sz]
            pose (list): pose array: [x y z qx qy qz qw]. The pose is relative to the shape's pose

        """
        ...

    def getShapeColor(
        self, shapeHandle: int, colorName: str, colorComponent: int
    ) -> Tuple[int, list]:
        """
            URL: https://manual.coppeliarobotics.com/en/sim/simGetShapeColor.htm
            Retrieves the color of a shape

            Args:
                shapeHandle (int): handle of the shape
                colorName (str): name of a color. If a non-empty name is provided, a specific color component is retrieved (e.g. if a shape is a compound shape. If colorName is
        @compound
        , then rgb data for every component of a compound shape is returned)
                colorComponent (int): color component

            Returns:
                result (int): 0 if the color name was not found in the shape, 1 otherwise
                rgbData (list): red, green and blue components of the color (3 values), or the transparency value (1 value)

        """
        ...

    def getShapeGeomInfo(self, shapeHandle: int) -> Tuple[int, int, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetShapeGeomInfo.htm
        Retrieves geometric information related to a shape

        Args:
            shapeHandle (int): handle of the shape

        Returns:
            result (int): bit-coded:
            pureType (int): the
            dimensions (list): array of 4 values giving information about the shape's dimensions (indexing (i) starts from 0 for Python and 1 for Lua):

        """
        ...

    def getShapeInertia(self, shapeHandle: int) -> Tuple[list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetShapeInertia.htm
        Retrieves the inertia information from a shape

        Args:
            shapeHandle (int): handle of the

        Returns:
            inertiaMatrix (list): No detailed return description.
            com (list): No detailed return description.

        """
        ...

    def getShapeMass(self, shapeHandle: int) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetShapeMass.htm
        Retrieves the mass of a shape

        Args:
            shapeHandle (int): handle of the

        Returns:
            mass (float): mass of the shape

        """
        ...

    def getShapeMesh(self, shapeHandle: int) -> Tuple[list, list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetShapeMesh.htm
        Retrieves a shape's mesh information

        Args:
            shapeHandle (int): handle of the shape. See

        Returns:
            vertices (list): array of vertices
            indices (list): array of indices
            normals (list): array of normals

        """
        ...

    def getShapeTextureId(self, shapeHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetShapeTextureId.htm
        Retrieves the texture ID of a texture that is applied to a specific shape

        Args:
            shapeHandle (int): handle of the shape.

        Returns:
            textureId (int): texture ID, or -1 if texture does not exist

        """
        ...

    def getShapeViz(self, shapeHandle: int, index: int) -> dict:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetShapeViz.htm Retrieves
        a shape's visual information.

        Args:
            shapeHandle (int): handle of the shape.
            index (int): 0-based index of the shape element to retrieve (compound shapes contain more than one shape element)

        Returns:
            data (dict): No detailed return description.

        """
        ...

    def getSimulationState(self) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetSimulationState.htm
        Retrieves current  simulation state

        Returns:
            simulationState (int): current

        """
        ...

    def getSimulationStopping(self) -> bool:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetSimulationStopping.htm
        Convenience function that returns true when the simulation is about to stop
        or stopped.

        Returns:
            stopping (bool): No detailed return description.

        """
        ...

    def getSimulationTime(self) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetSimulationTime.htm
        Retrieves the current simulation time

        """
        ...

    def getSimulationTimeStep(self) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetSimulationTimeStep.htm
        Retrieves the simulation time step (the simulation time (i.e. not real-time)
        that passes at each main script simulation pass). This value might not be
        constant for a given simulation.

        Returns:
            timeStep (float): No detailed return description.

        """
        ...

    def getSimulatorMessage(self) -> Tuple[int, list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetSimulatorMessage.htm
        Retrieves and removes the next message in the C/C++ or Lua message queues.
        Use this in a while-loop until all messages have been extracted. While the
        C/C++ interface has one single message queue, each Lua script has its own
        message queue. The C/C++ version of this function should only be called from
        the CoppeliaSim client application. A given message queue cannot hold more
        than 64 messages, unread messages will be discarded.

        Returns:
            message (int): simulator message
            auxiliaryData (list): array of numbers that describe the returned message in more details
            auxiliaryData2 (list): Description not provided

        """
        ...

    def getStackTraceback(self, scriptHandle: int) -> str:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetStackTraceback.htm Lua
        only. Retrieves and clears the last generated stack traceback for a script

        Args:
            scriptHandle (int): the script handle from which the traceback is desired. If omitted, then the calling script's traceback will be retrieved and cleared.

        Returns:
            stackTraceback (str): the stack traceback

        """
        ...

    def getstrProperty(
        self, target: int, propertyName: str, options: dict
    ) -> str:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetstrProperty.htm
        Fetches a str property (text)

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (str): property value

        """
        ...

    def getSystemTime(self) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetSystemTime.htm
        Retrieves the system time.

        Returns:
            systemTime (float): No detailed return description.

        """
        ...

    def getTextureId(self, textureName: str) -> Tuple[int, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetTextureId.htm
        Retrieves the texture ID of a specific texture

        Args:
            textureName (str): name of the texture ID to be retrieved

        Returns:
            textureId (int): the texture ID, or -1 if the texture does not exist
            resolution (list): an array of 2 values representing the resolution of the texture

        """
        ...

    def getUserVariables(self) -> list[str]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetUserVariables.htm Lua
        only. Returns all variables, except those set by CoppeliaSim.

        Returns:
            variables (list[str]): No detailed return description.

        """
        ...

    def getVector2Property(
        self, target: int, propertyName: str, options: dict
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetVector2Property.htm
        Fetches a vector2 property (double[2])

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (list): property value

        """
        ...

    def getVector3Property(
        self, target: int, propertyName: str, options: dict
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetVector3Property.htm
        Fetches a vector3 property (double[3])

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        Returns:
            propertyState (list): property value

        """
        ...

    def getVelocity(self, shapeHandle: int) -> Tuple[list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetVelocity.htm Retrieves
        the linear and/or angular velocity of the center of mass of a non-static
        shape. Data is provided by the selected physics engine

        Args:
            shapeHandle (int): handle of a dynamically enabled shape

        Returns:
            linearVelocity (list): array of 3 values that represent the linear velocity in absolute coordinates
            angularVelocity (list): array of 3 values that represent the angular velocity in absolute coordinates. The length of the vector represents the rotation speed, and the vector direction represents the rotation axis passing through the center of mass of the shape

        """
        ...

    def getVisionSensorDepth(
        self,
        sensorHandle: int,
        options: int,
        pos: list = [0, 0],
        size: list = [0, 0],
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetVisionSensorDepth.htm
        Reads the depth buffer of a vision sensor. The returned data doesn't make
        sense if sim.handleVisionSensor  wasn't called previously

        Args:
            sensorHandle (int): handle of the vision sensor
            options (int): options, bit-coded:
            pos (list): position of the depth buffer portion to retrieve. Defaults to [0 0]
            size (list): size of the depth buffer portion to retrieve. Defaults to [0 0], which corresponds to [resolutionX resolutionY]

        Returns:
            depth (bytes): the depth buffer. Use

        """
        ...

    def getVisionSensorImg(
        self,
        sensorHandle: int,
        options: int,
        rgbaCutOff: float,
        pos: list = [0, 0],
        size: list = [0, 0],
    ) -> Tuple[bytes, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetVisionSensorImg.htm
        Reads the image of a vision sensor. The returned data doesn't make sense if
        sim.handleVisionSensor  wasn't called previously

        Args:
            sensorHandle (int): handle of the vision sensor
            options (int): options, bit-coded:
            rgbaCutOff (float): when an RGBA image is returned, the alpha component is 255 for all depth values below
            pos (list): position of the image portion to retrieve. Default is [0 0]
            size (list): size of the image portion to retrieve. Default is [0 0], which corresponds to [resolutionX resolutionY]

        Returns:
            image (bytes): the image buffer. Use
            resolution (list): the vision sensor resolution

        """
        ...

    def getVisionSensorRes(self, sensorHandle: int) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGetVisionSensorRes.htm
        Returns the resolution of the vision sensor

        Args:
            sensorHandle (int): handle of the vision sensor

        Returns:
            resolution (list): No detailed return description.

        """
        ...

    def groupShapes(self, shapeHandles: list, merge: bool) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simGroupShapes.htm Groups
        (or merges) several shapes into a  compound shape  (or  simple shape )

        Args:
            shapeHandles (list): handles of the shapes to be grouped or merged. The last handle represents the shape that will accept the other shapes
            merge (bool): whether the shapes should be merged or grouped

        Returns:
            shapeHandle (int): the handle of the resulting compound shape, which is the last shape in

        """
        ...

    def handleAddOnScripts(self, callType: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simHandleAddOnScripts.htm
        Lua only. Calls a specific function in  add-ons . Should only be called from
        the  main script

        Args:
            callType (int): desired system call type (e.g.

        Returns:
            count (int): No detailed return description.

        """
        ...

    def handleDynamics(self, deltaTime: float) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simHandleDynamics.htm
        Handles the dynamics functionality in a scene

        Args:
            deltaTime (float): simulation time step, i.e.

        Returns:
            result (int): No detailed return description.

        """
        ...

    def handleEmbeddedScripts(self, callType: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simHandleEmbeddedScripts.htm
        Lua only. Calls a specific  system callback function  in simulation scripts
        and  customization scripts . Simulation- and customization scripts will be
        executed in a  precise order . This function should only be called from the
        main script

        Args:
            callType (int): desired system call type (e.g.

        Returns:
            scriptCount (int): No detailed return description.

        """
        ...

    def handleExtCalls(self) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simHandleExtCalls.htm
        Handles the message pump for threaded scripts

        """
        ...

    def handleGraph(self, graphHandle: int, time: float) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simHandleGraph.htm Handles a
        graph object (i.e. records another value for each curve, given that such
        value was provided via  sim.setGraphStreamValue

        Args:
            graphHandle (int): handle of the graph object.
            time (float): time where next value will be recorded at, usually the simulation time

        """
        ...

    def handleProximitySensor(
        self, sensorHandle: int
    ) -> Tuple[int, float, list, int, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simHandleProximitySensor.htm
        Handles (performs sensing, etc. of) a registered proximity sensor object

        Args:
            sensorHandle (int): handle of a proximity sensor object, or sim.handle_all or sim.handle_all_except_explicit

        Returns:
            res (int): 0 if nothing was detected
            dist (float): distance to the detected point
            point (list): array of 3 numbers indicating the relative coordinates of the detected point
            obj (int): handle of the object that was detected
            n (list): array of normal vector (normalized) of the detected surface. Relative to the sensor reference frame

        """
        ...

    def handleSandboxScript(self, callType: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simHandleSandboxScript.htm
        Lua only. Calls a specific function in the  sandbox .
        sim.handleSandboxScript should only be called from the  main script

        Args:
            callType (int): system call type (e.g.

        """
        ...

    def handleSimulationScripts(self, callType: int) -> int:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simHandleSimulationScripts.htm
        Lua only. Calls a specific  system callback function  in simulation scripts
        . Simulation scripts will be executed in a  precise order . This function
        should only be called from the  main script .

        Args:
            callType (int): the desired system call type (e.g.

        Returns:
            scriptCount (int): No detailed return description.

        """
        ...

    def handleVisionSensor(
        self, visionSensorHandle: int
    ) -> Tuple[int, list, list, Any]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simHandleVisionSensor.htm
        Handles (performs sensing, etc. of) a vision sensor object. It (1) clear
        previous computed image processing data, (2) reads an image and (3) performs
        image processing via the  vision callback functions (if the vision sensor is
        using an  external input  only (1) is performed)

        Args:
            visionSensorHandle (int): handle of a vision sensor object or sim.handle_all or sim.handle_all_except_explicit

        Returns:
            detectionCount (int): number of detections (number of vision sensors that triggered a detection)
            packet1 (list): default auxiliary value packet (15 auxiliary values: the minimum of [intensity red green blue depth], the maximum of [intensity red green blue depth], and the average of [intensity red green blue depth])
            packet2 (list): additional auxiliary value packet (e.g. from an image processing component)
            etc. (Any): Description not provided

        """
        ...

    def initScript(self, scriptHandle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simInitScript.htm
        Initializes/reinitializes a script. Operates in an asynchronous way, and
        cannot be called from within the script being reinitialized

        Args:
            scriptHandle (int): handle of the script to initialize/reinitialize

        """
        ...

    def insertObjectIntoOctree(
        self,
        octreeHandle: int,
        objectHandle: int,
        options: int,
        color: list,
        tag: int,
    ) -> int:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simInsertObjectIntoOctree.htm
        Inserts an object into an  OC tree , as voxels. Each voxel will store a
        color and a tag value

        Args:
            octreeHandle (int): handle of the OC tree
            objectHandle (int): handle of the object to insert. Only potentially
            options (int): reserved. Set to 0
            color (list): array of RGB triplet, specifying the red, green and blue color components (0 - 255). Can be None/nil
            tag (int): uint32 value, which is user-defined

        Returns:
            totalVoxelCnt (int): the total number of voxels in the OC tree

        """
        ...

    def insertObjectIntoPointCloud(
        self,
        pointCloudHandle: int,
        objectHandle: int,
        options: int,
        gridSize: float,
        color: list,
        duplicateTolerance: float,
    ) -> int:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simInsertObjectIntoPointCloud.htm
        Inserts an object into a  point cloud , as points

        Args:
            pointCloudHandle (int): handle of the point cloud
            objectHandle (int): handle of the object to insert. Only potentially
            options (int): reserved. Set to 0
            gridSize (float): when a shape is inserted, it will first be converted to an OC tree with a given grid or voxel size
            color (list): array containing an RGB triplet, specifying the red, green and blue color components (0 - 255). Can be None/nil.
            duplicateTolerance (float): a minimum distance tolerance value that is used to avoid duplicate points

        Returns:
            totalPointCnt (int): the total number of points in the point cloud

        """
        ...

    def insertPointsIntoPointCloud(
        self,
        pcHandle: int,
        options: int,
        points: list,
        color: list,
        duplicateTolerance: float,
    ) -> int:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simInsertPointsIntoPointCloud.htm
        Inserts points into a  point cloud

        Args:
            pcHandle (int): handle of the point cloud, can be combined with sim.handleflag_codedstr, when one wishes to provide point data as a float buffer, and color data as a char buffer
            options (int): bit-coded:
            points (list): array of point positions specified as x/y/z coordinates
            color (list): array of one or several RGB triplets, specifying the red, green and blue color components (0-255). Can be None/nil
            duplicateTolerance (float): a minimum distance tolerance value that is used to avoid duplicate points

        Returns:
            totalPointCnt (int): the total number of points in the point cloud

        """
        ...

    def insertVoxelsIntoOctree(
        self,
        octreeHandle: int,
        options: int,
        points: list,
        color: list,
        tag: list,
    ) -> int:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simInsertVoxelsIntoOctree.htm
        Inserts voxels into an  OC tree . Each voxel will store a color and a tag
        value

        Args:
            octreeHandle (int): handle of the OC tree, can be combined with sim.handleflag_codedstr, when one wishes to provide point data as a float buffer, color data as a char buffer and tag as an uint32 buffer
            options (int): bit-coded:
            points (list): array of voxel positions specified as x/y/z coordinates
            color (list): array of one or several RGB triplets, specifying the red, green and blue color components (0-255). Can be None/nil
            tag (list): array of one or several uint32 values, which are user-defined values. Can be None/nil

        Returns:
            totalVoxelCnt (int): the total number of voxels in the OC tree

        """
        ...

    def interpolateMatrices(
        self, matrixIn1: list, matrixIn2: list, interpolFactor: float
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simInterpolateMatrices.htm
        Computes the interpolated transformation matrix between matrixIn1 and
        matrixIn2. Quaternions are used internally

        Args:
            matrixIn1 (list): first input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
            matrixIn2 (list): second input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
            interpolFactor (float): interpolation factor, a value between 0.0 and 1.0 (0.0--> resultMatrix = matrixIn1, 1.0--> resultMatrix = matrixIn2)

        Returns:
            resultMatrix (list): the result matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

        """
        ...

    def interpolatePoses(
        self, poseIn1: list, poseIn2: list, interpolFactor: float
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simInterpolatePoses.htm
        Computes the interpolated pose between poseIn1 and poseIn2

        Args:
            poseIn1 (list): first input pose (array of 7 values [x y z qx qy qz qw])
            poseIn2 (list): second input pose (array of 7 values [x y z qx qy qz qw])
            interpolFactor (float): interpolation factor, a value between 0.0 and 1.0 (0.0--> resultPose = poseIn1, 1.0--> resultPose = poseIn2)

        Returns:
            resultPose (list): the result pose (array of 7 values [x y z qx qy qz qw])

        """
        ...

    def intersectPointsWithPointCloud(
        self, pcHandle: int, options: int, points: list, tolerance: float
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simIntersectPointsWithPointC
        loud.htm Removes points from a  point cloud , that do not intersect with the
        provided points (i.e. the result in the point cloud will be the intersection
        between the two sets of points). When a point cloud doesn't use an OC tree
        calculation structure, then this operation cannot be performed

        Args:
            pcHandle (int): handle of the point cloud
            options (int): bit-coded:
            points (list): array of point positions specified as x/y/z coordinates
            tolerance (float): distance used as a tolerance value

        Returns:
            totalPointCnt (int): the total number of points in the point cloud

        """
        ...

    def isDynamicallyEnabled(self, objectHandle: int) -> bool:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simIsDynamicallyEnabled.htm
        Checks whether a scene object is dynamically enabled, i.e. is being handled
        and simulated by the physics engine. Note that until the physics engine has
        parsed the scene in the first simulation step (i.e. the first time
        sim.handleDynamics  is called), no object will be dynamically enabled

        Args:
            objectHandle (int): Description not provided

        Returns:
            dynamicallyEnabled (bool): No detailed return description.

        """
        ...

    def isHandle(self, objectHandle: int) -> bool:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simIsHandle.htm Checks
        whether a general object handle is still valid. When a general object is
        destroyed (e.g. programmatically or via the user interface), then its
        related handle is not valid anymore and will trigger an error when used. Use
        this function to avoid triggering an error

        Args:
            objectHandle (int): handle of the object

        Returns:
            result (bool): whether the handle is valid

        """
        ...

    def launchExecutable(
        self, filename: str, parameters: str, showStatus: int
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simLaunchExecutable.htm
        Launches an executable. Similar to os.execute or io.popen, but is system
        independent.

        Args:
            filename (str): file name of the executable. If the filename starts with '@', then it will be considered as a system command, otherwise the current directory might be automatically prepended to the filename if it makes sense.
            parameters (str): optional input arguments
            showStatus (int): 0 to hide the application's window, 1 to show it. Works only with Windows OS.

        """
        ...

    def matrixToPose(self, matrix: list) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMatrixToPose.htm Converts
        a transformation matrix to a pose

        Args:
            matrix (list): input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

        Returns:
            pose (list): the output pose (array of 7 values [x y z qx qy qz qw])

        """
        ...

    def moduleEntry(self, handle: int, label: str, state: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simModuleEntry.htm Creates,
        modifies or destroys module menu entries. Those are user selectable items
        located in [Menu bar > Modules]. When selected, the corresponding script
        will have its  sysCall_moduleEntry callback function triggered, or
        sim_message_eventcallback_moduleentry  triggered

        Args:
            handle (int): handle of a module menu entry, or -1 to create one.
            label (str): label of the module entry. If handle is -1, then a path can be specified, in order to build sub-menus, e.g. "Menu\nSubmenu1\nSubmenu2\nLabel". Can be nullptr if handle is not -1.
            state (int): Bit-coded (is ignored if set to -1, -2 destroys an existing item):

        Returns:
            handle (int): No detailed return description.

        """
        ...

    def moveToConfig(self, params: dict) -> dict:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMoveToConfig.htm Executes
        a n-DoF motion using the  Ruckig online trajectory generator . This function
        can only be called from scripts running in a thread, since this is a
        blocking operation

        Args:
            params (dict): parameters of the function:

        Returns:
            data (dict): current motion state

        """
        ...

    def moveToConfig_cleanup(self, motionObject: dict) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMoveToConfig_cleanup.htm
        Destroys a motion object

        Args:
            motionObject (dict): handle of the motion object

        """
        ...

    def moveToConfig_init(self, params: dict) -> dict:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMoveToConfig_init.htm
        Initiates a n-DoF motion using the  Ruckig online trajectory generator

        Args:
            params (dict): parameters of the function:

        Returns:
            motionObject (dict): a motion object

        """
        ...

    def moveToConfig_step(self, motionObject: dict) -> Tuple[int, dict]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMoveToConfig_step.htm
        Steps a motion object

        Args:
            motionObject (dict): a motion object

        Returns:
            res (int): step result:
            data (dict): current motion state

        """
        ...

    def moveToPose(self, params: dict) -> dict:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMoveToPose.htm Executes
        an object motion using the  Ruckig online trajectory generator , by
        performing interpolations between two poses. The function can operate by
        handling 4 motion variables (x,y,z and angle between the two poses), or a
        single movement variable (t, which requires a metric to be specified for
        distance calculation between the two poses). This function can only be
        called from a script running in a thread, since this is a blocking operation

        Args:
            params (dict): parameters of the function:

        Returns:
            data (dict): current motion state

        """
        ...

    def moveToPose_cleanup(self, motionObject: dict) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMoveToPose_cleanup.htm
        Destroys a motion object

        Args:
            motionObject (dict): handle of the motion object

        """
        ...

    def moveToPose_init(self, params: dict) -> dict:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMoveToPose_init.htm
        Initiates an object motion using the  Ruckig online trajectory generator ,
        by performing interpolations between two poses. The function can operate by
        handling 4 motion variables (x,y,z and angle between the two poses), or a
        single movement variable (t, which requires a metric to be specified for
        distance calculation between the two poses)

        Args:
            params (dict): parameters of the function:

        Returns:
            motionObject (dict): a motion object

        """
        ...

    def moveToPose_step(self, motionObject: dict) -> Tuple[int, dict]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMoveToPose_step.htm Steps
        a motion object

        Args:
            motionObject (dict): a motion object

        Returns:
            res (int): step result:
            data (dict): current motion state

        """
        ...

    def multiplyMatrices(self, matrixIn1: list, matrixIn2: list) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMultiplyMatrices.htm
        Multiplies two transformation matrices

        Args:
            matrixIn1 (list): first input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
            matrixIn2 (list): second input matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

        Returns:
            resultMatrix (list): the result matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

        """
        ...

    def multiplyPoses(self, poseIn1: list, poseIn2: list) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMultiplyPoses.htm
        Multiplies two poses

        Args:
            poseIn1 (list): first input pose (array of 7 values [x y z qx qy qz qw])
            poseIn2 (list): second input pose (array of 7 values [x y z qx qy qz qw])

        Returns:
            resultPose (list): the result pose (array of 7 values [x y z qx qy qz qw])

        """
        ...

    def multiplyVector(self, quaternion: list, vector: list) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simMultiplyVector.htm
        Multiplies a vector with a quaternion, a pose, or a matrix (e.g. v = m * v)

        Args:
            quaternion (list): Description not provided
            vector (list): the original vector: an array of 3 * n values. Each triplet represents one vector to be multiplied

        Returns:
            resultVector (list): the result vector: an array of 3 * n values. Each triplet represents one vector

        """
        ...

    def packDoubleTable(
        self, doubleNumbers: list, startDoubleIndex: int, doubleCount: int
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simPackDoubleTable.htm Packs
        ab array of double floating-point numbers into a str

        Args:
            doubleNumbers (list): array of double floating-point numbers. Non-numbers will be packed as zero values
            startDoubleIndex (int): zero-based index from which on data should be packed. Can be omitted in which case 0 is used
            doubleCount (int): amount of doubles that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available doubles should be packed from the indicated startDoubleIndex)

        Returns:
            data (bytes): a buffer (values between 0 and 255) that contains packed double floating-point numbers

        """
        ...

    def packFloatTable(
        self, floatingNumbers: list, startFloatIndex: int, floatCount: int
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simPackFloatTable.htm Packs
        an array of floating-point numbers into a str

        Args:
            floatingNumbers (list): array containing floating-point numbers. Non-numbers will be packed as zero values
            startFloatIndex (int): zero-based index from which on data should be packed. Can be omitted in which case 0 is used
            floatCount (int): amount of floats that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available floats should be packed from the indicated startFloatIndex)

        Returns:
            data (bytes): a buffer (values between 0 and 255) that contains packed floating-point numbers

        """
        ...

    def packInt32Table(
        self, int32Numbers: list, startInt32Index: int, int32Count: int
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simPackInt32Table.htm Packs
        an array of int32 numbers into a str

        Args:
            int32Numbers (list): array containing int32 numbers. Non-numbers will be packed as zero values
            startInt32Index (int): zero-based index from which on data should be packed. Can be omitted in which case 0 is used
            int32Count (int): amount of int32s that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available int32s should be packed from the indicated startInt32Index)

        Returns:
            data (bytes): a buffer (values between 0 and 255) that contains packed int32 numbers

        """
        ...

    def packUInt16Table(
        self, uint16Numbers: list, startUint16Index: int, uint16Count: int
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simPackUInt16Table.htm Packs
        an array of uint16 numbers into a str

        Args:
            uint16Numbers (list): array containing uint16 numbers. Invalid uint16 numbers will be packed in an undefined manner.
            startUint16Index (int): zero-based index from which on data should be packed. Can be omitted in which case 0 is used
            uint16Count (int): amount of uint16s that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available uint16s should be packed from the indicated startUint16Index)

        Returns:
            data (bytes): a buffer (values between 0 and 255) that contains packed uint16 numbers

        """
        ...

    def packUInt32Table(
        self, uint32Numbers: list, startUint32Index: int, uint32Count: int
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simPackUInt32Table.htm Packs
        an array of uint32 numbers into a str

        Args:
            uint32Numbers (list): array containing uint32 numbers. Non-numbers will be packed as zero values
            startUint32Index (int): zero-based index from which on data should be packed. Can be omitted in which case 0 is used
            uint32Count (int): amount of uint32s that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available uint32s should be packed from the indicated startUint32Index)

        Returns:
            data (bytes): a buffer (values between 0 and 255) that contains packed uint32 numbers

        """
        ...

    def packUInt8Table(
        self, uint8Numbers: list, startUint8Index: int, uint8count: int
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simPackUInt8Table.htm Packs
        an array of uint8 numbers into a str

        Args:
            uint8Numbers (list): array containing uint8 numbers. Invalid byte number will be packed in an undefined manner.
            startUint8Index (int): zero-based index from which on data should be packed. Can be omitted in which case 0 is used
            uint8count (int): amount of uint8s that should be packed. Can be omitted in which case 0 is used (which indicates that the maximum available uint8s should be packed from the indicated startUint8Index)

        Returns:
            data (bytes): a buffer (values between 0 and 255) that contains the uint8 numbers

        """
        ...

    def pauseSimulation(self) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simPauseSimulation.htm
        Requests a pause of a simulation

        """
        ...

    def poseToMatrix(self, pose: list) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simPoseToMatrix.htm Converts
        a pose to a transformation matrix

        Args:
            pose (list): input pose (array of 7 values [x y z qx qy qz qw])

        Returns:
            matrix (list): the output matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])

        """
        ...

    def pushUserEvent(
        self, event: str, handle: int, eventData: dict, options: int
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simPushUserEvent.htm Pushes
        a user-triggered event. Messages are received asynchronously via the
        sysCall_event  callback function  and via the plugin
        sim_message_eventcallback_events  message call

        Args:
            event (str): event name
            handle (int): optional handle associated with the event. Can be -1
            eventData (dict): event data
            options (int): bit-coded:

        """
        ...

    def quitSimulator(self) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simQuitSimulator.htm
        Triggers a quit signal after which the application eventually ends

        """
        ...

    def readForceSensor(self, objectHandle: int) -> Tuple[int, list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simReadForceSensor.htm Reads
        the force and torque applied to a force sensor (filtered values are read)

        Args:
            objectHandle (int): handle of the object (must be a force sensor). Can be combined with

        Returns:
            result (int): bit-coded:
            forceVector (list): array of 3 values (applied forces along the sensor's x, y and z-axes)
            torqueVector (list): array of 3 values (applied torques about the sensor's x, y and z-axes)

        """
        ...

    def readProximitySensor(
        self, sensorHandle: int
    ) -> Tuple[int, float, list, int, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simReadProximitySensor.htm
        Reads the state of a proximity sensor. This function doesn't perform
        detection, it merely reads the result from a previous call to
        sim.handleProximitySensor

        Args:
            sensorHandle (int): handle of a proximity sensor

        Returns:
            res (int): detection state (0 or 1)
            dist (float): distance to the detected point
            point (list): array of 3 numbers indicating the relative coordinates of the detected point
            obj (int): handle of the object that was detected
            n (list): normal vector (normalized) of the detected surface. Relative to the sensor reference frame

        """
        ...

    def readTexture(
        self,
        textureId: int,
        options: int,
        posX: int,
        posY: int,
        sizeX: int,
        sizeY: int,
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simReadTexture.htm Retrieves
        the RGB data (or a portion of it) related to a specific texture

        Args:
            textureId (int): ID of the texture. See also
            options (int): reserved for future functionality. Set to zero.
            posX (int): Description not provided
            posY (int): x/y position of the texture portion to retrieve. Set to [0 0] to retrieve the full texture
            sizeX (int): Description not provided
            sizeY (int): x/y size of the texture portion to retrieve. Set to [0 0] to retrieve the full texture

        Returns:
            textureData (bytes): texture data

        """
        ...

    def readVisionSensor(
        self, visionSensorHandle: int
    ) -> Tuple[int, list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simReadVisionSensor.htm
        Reads the state of a vision sensor. This function doesn't perform detection,
        it merely reads the result from a previous call to  sim.handleVisionSensor

        Args:
            visionSensorHandle (int): handle of a vision sensor object

        Returns:
            result (int): detection state (0 or 1), or -1 if
            packet1 (list): default auxiliary packet of 15 auxiliary values: the minimum of [intensity red green blue depth], the maximum of [intensity red green blue depth], and the average of [intensity red green blue depth]
            packet2 (list): additional auxiliary value packet (e.g. from an image processing component)

        """
        ...

    def refreshDialogs(self, refreshDegree: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simRefreshDialogs.htm
        Refreshes CoppeliaSim's internal dialogs. Calling   will not trigger a
        sim.message_eventcallback_refreshdialogs  message

        Args:
            refreshDegree (int): refresh degree (0=light, 1=medium, 2=full)

        """
        ...

    def releaseLock(self) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simReleaseLock.htm
        Counterpart function to  sim.acquireLock . Unlocking is cumulative

        """
        ...

    def removeDrawingObject(self, objectHandle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simRemoveDrawingObject.htm
        Removes a previously added drawing object

        Args:
            objectHandle (int): handle of a previously added drawing object

        """
        ...

    def removeModel(self, objectHandle: int, delayedRemoval: bool) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simRemoveModel.htm Removes a
        model from the scene

        Args:
            objectHandle (int): handle of the model (i.e. object tagged as model) to remove
            delayedRemoval (bool): whether the removal should be delayed (e.g. when a script destroys itself). Defaults to false

        Returns:
            removedCnt (int): number of removed objects (a model might contain several objects)

        """
        ...

    def removeObjects(
        self, objectHandles: list[int], delayedRemoval: bool
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simRemoveObjects.htm Removes
        one or several objects from the scene

        Args:
            objectHandles (list[int]): handles of the objects to remove
            delayedRemoval (bool): whether the removal should be delayed (e.g. when a script destroys itself). Defaults to false

        """
        ...

    def removeParticleObject(self, objectHandle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simRemoveParticleObject.htm
        Removes a previously added particle object

        Args:
            objectHandle (int): handle of a previously added particle object. sim.handle_all removes all particle objects from the scene

        """
        ...

    def removePointsFromPointCloud(
        self,
        pointCloudHandle: int,
        options: int,
        points: list,
        tolerance: float,
    ) -> int:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simRemovePointsFromPointCloud.htm
        Removes points from a  point cloud . When a point cloud doesn't use an OC
        tree calculation structure, then individual points cannot be removed, only
        all points can be removed in that case

        Args:
            pointCloudHandle (int): handle of the point cloud
            options (int): bit-coded:
            points (list): point positions specified as x/y/z coordinates. Set to None/nil to remove all points
            tolerance (float): distance used as a tolerance value

        Returns:
            totalPointCnt (int): total number of points in the point cloud

        """
        ...

    def removeProperty(
        self, target: int, propertyName: str, options: dict
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simRemoveProperty.htm
        Removes a removable property

        Args:
            target (int): target item
            propertyName (str): property name
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def removeVoxelsFromOctree(
        self, octreeHandle: int, options: int, points: list
    ) -> int:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simRemoveVoxelsFromOctree.htm
        Removes voxels from an  OC tree

        Args:
            octreeHandle (int): handle of the OC tree
            options (int): bit-coded:
            points (list): voxel positions specified as x/y/z coordinates. Set to None/nil to remove all voxels

        Returns:
            totalVoxelCnt (int): total number of voxels in the OC tree

        """
        ...

    def resamplePath(
        self,
        path: list,
        pathLengths: list,
        finalConfigCnt: int,
        method: dict = {"type": "linear", "strength": 1.0, "forceOpen": False},
        types: list | None = None,
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simResamplePath.htm Returns
        a resampled path

        Args:
            path (list): path, specified in row-major order, e.g. a path containing two 3D poses (position+quaternion) would be [x1 y1 z1 qx1 qy1 qz1 qw1 x2 y2 z2 qx2 qy2 qz2 qw2]
            pathLengths (list): lengths of a path. Each path point should have a corresponding length value (as the distance from the path's first point, along the path). See also
            finalConfigCnt (int): number of points or configurations the resampled path should contain
            method (dict): optional map specifying the type of interpolation (linear or quadraticBezier), and whether the path should be considered as open, even if the first and last path points overlap, and the bezier strength (0.05-1.0)
            types (list): optional array specifying the type of each configuration value/dimension: 0=cartesian value, 1=2pi-cyclic value, 2=quaternion value. e.g. a configuration representing 3D poses should use a types argument [0 0 0 2 2 2 2], a configuration representing revolute and cyclic joints should use a types argument [1 1 1 ...]

        Returns:
            outputPath (list): the resampled path

        """
        ...

    def resetDynamicObject(self, objectHandle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simResetDynamicObject.htm
        Dynamically resets an object that is dynamically simulated. This means that
        the object representation in the dynamics engine is removed, and added
        again. This can be useful when the set-up of a dynamically simulated chain
        needs to be modified during simulation (e.g. joint or shape attachement
        position/orientation changed)

        Args:
            objectHandle (int): handle of the object. Can be combined with

        """
        ...

    def resetGraph(self, graphHandle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simResetGraph.htm Resets a
        graph object (i.e. clears all its data streams)

        Args:
            graphHandle (int): handle of the graph object

        """
        ...

    def resetProximitySensor(self, sensorHandle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simResetProximitySensor.htm
        Clears the detection state, detection color, detection segments, etc. of a
        proximity sensor object

        Args:
            sensorHandle (int): handle of the proximity sensor object or sim.handle_all or sim.handle_all_except_explicit

        """
        ...

    def resetVisionSensor(self, sensorHandle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simResetVisionSensor.htm
        Clears the detection state, etc. of a proximity sensor object

        Args:
            sensorHandle (int): handle of the vision sensor object or sim.handle_all or sim.handle_all_except_explicit

        """
        ...

    def restoreEntityColor(self, originalColorData: list) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simRestoreEntityColor.htm
        Restores the color of an  entity , previously modified with
        sim.changeEntityColor

        Args:
            originalColorData (list): the data returned from a call to

        """
        ...

    def rotateAroundAxis(
        self, poseIn: list, axis: list, axisPos: list, angle: float
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simRotateAroundAxis.htm
        Rotates a pose or transformation matrix around a random axis in space. This
        function, when used in combination with  sim.getRotationAxis , can be used
        to build interpolations between poses or transformation matrices

        Args:
            poseIn (list): Description not provided
            axis (list): the axis vector in absolute coordinates to rotate around
            axisPos (list): the position of the rotation axis in absolute coordinates
            angle (float): the amount of rotation to perform

        Returns:
            poseOut (list): No detailed return description.

        """
        ...

    def ruckigPos(
        self,
        dofs: int,
        baseCycleTime: float,
        flags: int,
        currentPosVelAccel: list,
        maxVelAccelJerk: list,
        selection: list,
        targetPosVel: list,
    ) -> int:
        """
            URL: https://manual.coppeliarobotics.com/en/sim/simRuckigPos.htm Executes a
            call to the  Ruckig online trajectory generator . The Ruckig online
            trajectory generator provides instantaneous trajectory generation
            capabilities for motion control systems. This function prepares a position-
            based trajectory generation object, that can then be calculated with
            sim.ruckigStep . When this object is not needed anymore, remove it with
            sim.ruckigRemove

            Args:
                dofs (int): number of degrees of freedom (n).
                baseCycleTime (float): smallest expected cycle time. The cycle time should always be a multiple of baseCycleTime. Use a value of 0.0001 (0.1ms).
                flags (int): Ruckig flags
        . -1 for default flags.
                currentPosVelAccel (list): current position, velocity and acceleration: [pos_1 ... pos_n vel_1 ... vel_n accel_1 ... accel_n] (one value for each DoF)
                maxVelAccelJerk (list): maximum allowed velocity, acceleration and jerk: [maxV_1 ... maxV_n maxA_1 ... maxA_n maxJ_1 ... maxJ_n]. If sim.ruckig_minvel is specified in flags, then maxVelAccelJerk should contain following additional values: [minV_1 ... minV_n]. If sim.ruckig_minaccel is specified in flags, then maxVelAccelJerk should contain following additional values: [minA_1 ... minA_n]
                selection (list): selection vector (one value for each DoF). For a default behaviour, fill the vector with non-zero values.
                targetPosVel (list): target position and velocity: [tPos_1 ... tPos_n tVel_1 ... tVel_n]

            Returns:
                handle (int): the handle to the created object

        """
        ...

    def ruckigRemove(self, handle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simRuckigRemove.htm Removes
        an object previously created via  sim.ruckigPos or  sim.ruckigVel .

        Args:
            handle (int): handle of the object created via

        """
        ...

    def ruckigStep(
        self, handle: int, cycleTime: float
    ) -> Tuple[int, list, float]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simRuckigStep.htm Executes a
        call to the  Ruckig online trajectory generator . The Ruckig online
        trajectory generator provides instantaneous trajectory generation
        capabilities for motion control systems. This function steps forward a
        trajectory generation algorithm previously prepared via  sim.ruckigPos  or
        sim.ruckigVel

        Args:
            handle (int): handle of the object created via
            cycleTime (float): cycle time or simulation step. Should always be a multiple of the base cycle time

        Returns:
            result (int): return value of the update function in the motion library:
            newPosVelAccel (list): Description not provided
            synchronizationTime (float): Description not provided

        """
        ...

    def ruckigVel(
        self,
        dofs: int,
        baseCycleTime: float,
        flags: int,
        currentPosVelAccel: list,
        maxAccelJerk: list,
        selection: list,
        targetVel: list,
    ) -> int:
        """
            URL: https://manual.coppeliarobotics.com/en/sim/simRuckigVel.htm Executes a
            call to the  Ruckig online trajectory generator . The Ruckig online
            trajectory generator provides instantaneous trajectory generation
            capabilities for motion control systems. This function prepares a velocity-
            based trajectory generation object, that can then be calculated with
            sim.ruckigStep . When this object is not needed anymore, remove it with
            sim.ruckigRemove

            Args:
                dofs (int): number of degrees of freedom (n).
                baseCycleTime (float): smallest expected cycle time. The cycle time should always be a multiple of baseCycleTime. Use a value of 0.0001 (0.1ms).
                flags (int): Ruckig flags
        . -1 for default flags.
                currentPosVelAccel (list): current position, velocity and acceleration: [pos_1 ... pos_n vel_1 ... vel_n accel_1 ... accel_n] (one value for each DoF)
                maxAccelJerk (list): maximum allowed acceleration and jerk: [maxA_1 ... maxA_n maxJ_1 ... maxJ_n]. If sim.ruckig_minaccel is specified in flags, then maxAccelJerk should contain following additional values: [minA_1 ... minA_n]
                selection (list): selection vector (one value for each DoF). For a default behaviour, fill the vector with non-zero values.
                targetVel (list): target velocity (one value for each DoF)

            Returns:
                handle (int): the handle of the created object

        """
        ...

    def saveImage(
        self,
        image: bytes,
        resolution: list,
        options: int,
        filename: str,
        quality: int,
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSaveImage.htm Saves an
        image to file or to memory

        Args:
            image (bytes): image (in rgb, rgba or greyscale format)
            resolution (list): x/y resolution of the provided image.
            options (int): bit-coded:
            filename (str): name of the file to write. The file extension indicates the format. If the filename only contains '.ext', where ext represents the file format, then the image will be saved to memory
            quality (int): quality of the written image: 0 for best compression, 100 for largest file. Use -1 for default behaviour.

        Returns:
            imgBuffer (bytes): a buffer containing the image in packed format (e.g. png, jpg, etc.), if the image was specified to be saved to memory.

        """
        ...

    def saveModel(self, baseOfModelHandle: int, filename: str) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSaveModel.htm Saves a
        model (an object marked as "Object is model base" and all other objects in
        its hierarchy tree). Any existing file with same name will be overwritten

        Args:
            baseOfModelHandle (int): handle of an object marked as "Object is model base"
            filename (str): model filename. The filename extension is required (

        Returns:
            buffer (bytes): No detailed return description.

        """
        ...

    def saveScene(self, filename: str) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSaveScene.htm Saves a
        scene. Any existing file with same name will be overwritten

        Args:
            filename (str): scene filename. The filename extension is required. With None/nil, a buffer representing the serialized scene is returned

        Returns:
            buffer (bytes): if filename is None/nil, a buffer representing the serialized scene

        """
        ...

    def scaleObject(
        self,
        objectHandle: int,
        xScale: float,
        yScale: float,
        zScale: float,
        options: int,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simScaleObject.htm Scales
        specified objects in a non-isometric fashion, if possible. Only non-compound
        shapes can be non-isometrically scaled. Some primitive shapes can have some
        constraints between their axes

        Args:
            objectHandle (int): handle of the object to scale
            xScale (float): Description not provided
            yScale (float): Description not provided
            zScale (float): scaling factors along the object's x, y and z-axis
            options (int): keep at 0

        """
        ...

    def scaleObjects(
        self,
        objectHandles: list,
        scalingFactor: float,
        scalePositionsToo: bool,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simScaleObjects.htm Scales
        specified objects. All related values are automatically scaled appropriately
        (e.g. masses, forces, etc.)

        Args:
            objectHandles (list): array containing the handles of the objects to scale. If an object is a model base, all its child objects will also be scaled
            scalingFactor (float): scaling factor
            scalePositionsToo (bool): if true, selected object's positions will also be scaled

        """
        ...

    def scheduleExecution(
        self, f: Any, args: list, timePoint: float, simTime: bool
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simScheduleExecution.htm
        Schedules execution of a function

        Args:
            f (func): function to call
            args (list): arguments to the function
            timePoint (float): time when the function should execute
            simTime (bool): simulation or real-time scheduling

        Returns:
            id (int): id of the scheduled execution function

        """
        ...

    def serialCheck(self, portHandle: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSerialCheck.htm Reads how
        many bytes are waiting to be read on a serial port (RS-232)

        Args:
            portHandle (int): handle returned by the

        Returns:
            result (int): the number of bytes that are waiting to be read

        """
        ...

    def serialClose(self, portHandle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSerialClose.htm Closes a
        serial port (RS-232)

        Args:
            portHandle (int): handle returned by

        """
        ...

    def serialOpen(self, portstr: str, baudRate: int) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSerialOpen.htm Opens a
        serial port (RS-232) for communication. When called from a script, the
        function can only be called when the simulation is running (and in that case
        the port is automatically closed at simulation stop)

        Args:
            portstr (str): str specifying the port to open. Under Windows, use something similar to "\\.\\COM1". Under MacOS and Linux, use something similar to "/dev/*" (check the "/dev" folder to know what file to specify). Under Linux, you might have to launch CoppeliaSim with super user priviledges in order to access the serial port
            baudRate (int): baudrate

        Returns:
            result (int): the port handle

        """
        ...

    def serialRead(
        self,
        portHandle: int,
        dataLengthToRead: int,
        blockingOperation: bool,
        closingstr: str,
        timeout: float,
    ) -> str:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSerialRead.htm Reads from
        a previously opened serial port (RS-232). The C version of the function
        cannot be blocking

        Args:
            portHandle (int): handle returned by the
            dataLengthToRead (int): maximum data length that should be read
            blockingOperation (bool): if true and the calling script is running in a thread, then the function only returns when the desired data length was read (or if the closingstr was met, or if there was a timeout (see next arguments)
            closingstr (str): str (containing any byte value) can be specified, that will break from the blocking operation if a match was found in the incoming data. Useful when you know that a data packet is always ended with a given signature. Can be an empty str for default operation.
            timeout (float): duration after which the blocking operation will be aborted, or 0 if the timeout is infinite

        Returns:
            data (str): a str containing read data (excluding the closingstr if it was specified and found)

        """
        ...

    def serialSend(self, portHandle: int, data: Any) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSerialSend.htm Writes
        data to a previously opened serial port (RS-232)

        Args:
            portHandle (int): handle returned by the
            data (buffer): pointer to the data that should be sent

        Returns:
            charsSent (int): the effective data length that was written

        """
        ...

    def setAutoYieldDelay(self, dt: float) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetAutoYieldDelay.htm
        Allows specifying a thread interruption or yield delay, that will be
        automatically enforced by the system (preemptive threading). By default this
        value is 2 ms

        Args:
            dt (float): desired execution time, before an interruption or yield occurs

        """
        ...

    def setBoolProperty(
        self,
        target: int,
        propertyName: str,
        propertyState: bool,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetBoolProperty.htm Sets
        a boolean property

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (bool): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setBufferProperty(
        self,
        target: int,
        propertyName: str,
        propertyState: bytes,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetBufferProperty.htm
        Sets a buffer property

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (bytes): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setColorProperty(
        self,
        target: int,
        propertyName: str,
        propertyState: list,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetColorProperty.htm Sets
        a color property (float[3])

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (list): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setEventFilters(self, filters: dict) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetEventFilters.htm
        Specifies filters for the sysCall_event callback. Operates on a per script
        basis

        Args:
            filters (dict): filters, e.g.:

        """
        ...

    def setExplicitHandling(
        self, objectHandle: int, explicitFlags: int
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetExplicitHandling.htm
        Sets the explicit handling flags for a scene object

        Args:
            objectHandle (int): handle of a scene object.
            explicitFlags (int): explicit handling flags. For now only bit 0 is used

        """
        ...

    def setFloatArrayProperty(
        self,
        target: int,
        propertyName: str,
        propertyState: list,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetFloatArrayProperty.htm
        Sets a float array property (double[])

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (list): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setFloatProperty(
        self,
        target: int,
        propertyName: str,
        propertyState: float,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetFloatProperty.htm Sets
        a float property (double)

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (float): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setGraphStreamTransformation(
        self,
        graphHandle: int,
        streamId: int,
        trType: int,
        mult: float,
        off: float,
        movingAvgPeriod: int,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetGraphStreamTransformat
        ion.htm Applies a transformation to a graph stream

        Args:
            graphHandle (int): handle of the graph
            streamId (int): id of the stream
            trType (int): stream transformation
            mult (float): multiplication factor
            off (float): an offset
            movingAvgPeriod (int): moving average period. Set to 1 for no moving average

        """
        ...

    def setGraphStreamValue(
        self, graphHandle: int, streamId: int, value: float
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetGraphStreamValue.htm
        Sets the next value to be recorded for a graph stream

        Args:
            graphHandle (int): handle of the graph object
            streamId (int): id of the stream
            value (float): value to set. Omitting to set a value for a corresponding

        """
        ...

    def setIntArray2Property(
        self,
        target: int,
        propertyName: str,
        propertyState: list,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetIntArray2Property.htm
        Sets an int[2] property

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (list): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setIntArrayProperty(
        self,
        target: int,
        propertyName: str,
        propertyState: list,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetIntArrayProperty.htm
        Sets an int array property (int[])

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (list): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setIntProperty(
        self, target: int, propertyName: str, propertyState: int, options: dict
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetIntProperty.htm Sets
        an int32 property

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (int): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setJointDependency(
        self,
        jointHandle: int,
        masterJointHandle: int,
        offset: float,
        multCoeff: float,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetJointDependency.htm
        Sets a joint dependent of another joint. The dependent joint should first be
        set into dependent mode via  sim.setJointMode

        Args:
            jointHandle (int): handle of the joint to become slave
            masterJointHandle (int): handle of the joint to become master, or -1 to free the slave joint from dependency
            offset (float): offset in equation slave = offset + master * multCoeff
            multCoeff (float): coeff in equation slave = offset + master * multCoeff

        """
        ...

    def setJointInterval(
        self, objectHandle: int, cyclic: bool, interval: list
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetJointInterval.htm Sets
        the interval parameters of a joint (i.e. range values). The attributes or
        interval parameters might have no effect, depending on the joint-type

        Args:
            objectHandle (int): handle of the joint object
            cyclic (bool): indicates whether the joint is cyclic. Only revolute joints with a lead of 0 can be cyclic
            interval (list): joint limits. The first value is the joint lower limit, the second value is the joint range (i.e. the upper limit is lower limit + range)

        """
        ...

    def setJointMode(self, jointHandle: int, jointMode: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetJointMode.htm Sets the
        operation mode of a joint

        Args:
            jointHandle (int): handle of the joint object
            jointMode (int): joint mode

        """
        ...

    def setJointPosition(self, objectHandle: int, position: float) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetJointPosition.htm Sets
        the linear/angular position of a joint. Cannot be used with spherical joints
        (use  sim.setObjectChildPose  instead)

        Args:
            objectHandle (int): handle of the joint object
            position (float): linear/angular position of the joint

        """
        ...

    def setJointTargetForce(
        self, objectHandle: int, forceOrTorque: float
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetJointTargetForce.htm
        Sets the force or torque that a joint can exert

        Args:
            objectHandle (int): handle of the joint object
            forceOrTorque (float): maximum force or torque the joint can exert

        """
        ...

    def setJointTargetPosition(
        self,
        objectHandle: int,
        targetPosition: float,
        motionParams: list[float] = [],
    ) -> None:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simSetJointTargetPosition.htm
        Sets the target linear/angular position of a joint. When in kinematic mode,
        the joint moves according to a motion profile that respects maximum
        velocity, acceleration and jerk values. In dynamic and position/custom
        control mode, the controller is instructed about the desired position

        Args:
            objectHandle (int): handle of the joint object
            targetPosition (float): target position of the joint
            motionParams (list[float]): when in kinematic mode: the maximum allowed velocity, acceleration and jerk. When in dynamics mode with position control and motion profile enabled, the maximum allowed velocity, acceleration and jerk. Can be None/nil for default values. See also the

        """
        ...

    def setJointTargetVelocity(
        self,
        objectHandle: int,
        targetVelocity: float,
        motionParams: list[float] = [],
    ) -> None:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simSetJointTargetVelocity.htm
        Sets the target linear/angular velocity of a non-spherical joint. When in
        kinematic mode, the joint moves according to a motion profile that respects
        maximum acceleration and jerk values. In dynamic and velocity control mode,
        the controller is instructed about the desired velocity

        Args:
            objectHandle (int): handle of the joint object
            targetVelocity (float): target velocity of the joint
            motionParams (list[float]): when the joint is in kinematic mode: the maximum allowed acceleration and jerk. When in dynamic mode with motion profile control enabled: the maximum allowed acceleration and jerk. Can be None/nil for default values. See also the

        """
        ...

    def setLinkDummy(self, dummyHandle: int, linkedDummyHandle: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetLinkDummy.htm Defines
        (or breaks) a dummy-dummy link pair. Useful to create dynamic loop closure
        constraints on the fly (among others)

        Args:
            dummyHandle (int): handle of the first dummy in the dummy-dummy link pair
            linkedDummyHandle (int): handle of the second dummy in the dummy-dummy link pair. Set to -1 to unlink the first dummy

        """
        ...

    def setLongProperty(
        self, target: int, propertyName: str, propertyState: int, options: dict
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetLongProperty.htm Sets
        an int64 property

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (int): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setNavigationMode(self, navigationMode: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetNavigationMode.htm
        Sets the navigation and selection mode for the mouse

        Args:
            navigationMode (int): mouse navigation mode

        """
        ...

    def setObjectAlias(self, objectHandle: int, objectAlias: str) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetObjectAlias.htm Sets
        the alias of an object

        Args:
            objectHandle (int): handle of the object
            objectAlias (str): alias of the object. Allowed characters include 0-9, a-z, A-Z, and underscores. Illegal characters are replaced with underscores

        """
        ...

    def setObjectChildPose(self, objectHandle: int, pose: list) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetObjectChildPose.htm
        Can be used to set a spherical joint's rotational transformation (the
        translational part is ignored)

        Args:
            objectHandle (int): handle of the object
            pose (list): the pose (array of 7 values [x y z qx qy qz qw])

        """
        ...

    def setObjectColor(
        self, objectHandle: int, index: int, colorComponent: int, rgbData: list
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetObjectColor.htm Sets
        the color of a scene object

        Args:
            objectHandle (int): handle of the object
            index (int): zero-based index of the color, if the object has several colors
            colorComponent (int): color component
            rgbData (list): red, green and blue components of the color (3 values)

        """
        ...

    def setObjectHierarchyOrder(self, objectHandle: int, order: int) -> None:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simSetObjectHierarchyOrder.htm
        Moves an object up or down among its siblings in the scene hierarchy

        Args:
            objectHandle (int): the handle of the object
            order (int): the desired zero-based position

        """
        ...

    def setObjectMatrix(
        self, objectHandle: int, matrix: list, relativeToObjectHandle: int
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetObjectMatrix.htm Sets
        the transformation matrix of an object. Dynamically simulated objects,
        together with their hierarchy tree, are dynamically reset (this however does
        not apply to static shapes)

        Args:
            objectHandle (int): handle of the object. Can be combined with sim.handleflag_reljointbaseframe
            matrix (list): the matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2])
            relativeToObjectHandle (int): indicates relative to which reference frame the matrix is specified. Specify sim.handle_world to set the absolute transformation matrix, sim.handle_inverse to set the inverse of the absolute transformation matrix, sim.handle_parent to set the transformation matrix relative to the object's parent, or an object handle relative to whose reference frame the transformation matrix is specified. If this handle is the handle of a joint, then the matrix is applied relative to the joint's moving frame (unless

        """
        ...

    def setObjectOrientation(
        self, objectHandle: int, eulerAngles: list, relativeToObjectHandle: int
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetObjectOrientation.htm
        Sets the orientation ( Euler angles ) of an object. Dynamically simulated
        objects, together with their hierarchy tree, are dynamically reset (this
        however does not apply to static shapes)

        Args:
            objectHandle (int): handle of the object. Can be combined with sim.handleflag_reljointbaseframe
            eulerAngles (list): Euler angles (alpha, beta and gamma)
            relativeToObjectHandle (int): indicates relative to which reference frame the orientation is specified. Specify sim.handle_world to set the absolute orientation, sim.handle_parent to set the orientation relative to the object's parent, or an object handle relative to whose reference frame the orientation is specified. If this handle is the handle of a joint, then the orientation is applied relative to the joint's moving frame (unless

        """
        ...

    def setObjectParent(
        self, objectHandle: int, parentObjectHandle: int, keepInPlace: bool
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetObjectParent.htm Sets
        an object's parent object. Dynamically simulated objects, together with
        their hierarchy tree, are dynamically reset (this however does not apply to
        static shapes)

        Args:
            objectHandle (int): handle of the object that will become child of the parent object. Can be or-combined with
            parentObjectHandle (int): handle of the object that will become parent, or -1 if the object should become parentless. In an assembly operation, the assembly dummy on the parent object should be specified instead
            keepInPlace (bool): indicates whether the object's absolute pose should stay same

        """
        ...

    def setObjectPose(
        self, objectHandle: int, pose: list, relativeToObjectHandle: int
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetObjectPose.htm Sets
        the pose of an object. Dynamically simulated objects, together with their
        hierarchy tree, are dynamically reset (this however does not apply to static
        shapes)

        Args:
            objectHandle (int): handle of the object. Combine with sim.handleflag_wxyzquat to provide the quaternion as [qw qx qy qz] order instead of [qx qy qz qw] order. Can also be combined with sim.handleflag_reljointbaseframe
            pose (list): the pose (array of 7 values [x y z qx qy qz qw])
            relativeToObjectHandle (int): indicates relative to which reference frame the pose is specified. Specify sim.handle_world to set the absolute pose, sim.handle_inverse to set the inverse of the absolute pose, sim.handle_parent to set the pose relative to the object's parent, or an object handle relative to whose reference frame the pose is specified. If this handle is the handle of a joint, then the pose is applied relative to the joint's moving frame (unless

        """
        ...

    def setObjectPosition(
        self, objectHandle: int, position: list, relativeToObjectHandle: int
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetObjectPosition.htm
        Sets the position (x, y and z-coordinates) of an object. Dynamically
        simulated objects, together with their hierarchy tree, are dynamically reset
        (this however does not apply to static shapes)

        Args:
            objectHandle (int): handle of the object. Can be combined with sim.handleflag_reljointbaseframe
            position (list): coordinates of the object
            relativeToObjectHandle (int): indicates relative to which reference frame the position is specified. Specify sim.handle_world to set the absolute position, sim.handle_parent to set the position relative to the object's parent, or an object handle relative to whose reference frame the position is specified. If this handle is the handle of a joint, then the position is applied relative to the joint's moving frame (unless

        """
        ...

    def setObjectQuaternion(
        self, objectHandle: int, quaternion: list, relativeToObjectHandle: int
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetObjectQuaternion.htm
        Sets the quaternion of an object. Dynamically simulated objects, together
        with their hierarchy tree, are dynamically reset (this however does not
        apply to static shapes)

        Args:
            objectHandle (int): handle of the object. Combine with sim.handleflag_wxyzquat to provide the quaternion as [qw qx qy qz] order instead of [qx qy qz qw] order. Can also be combined with sim.handleflag_reljointbaseframe
            quaternion (list): the quaternion (array of 4 values [qx qy qz qw])
            relativeToObjectHandle (int): indicates relative to which reference frame the orientation is specified. Specify sim.handle_world to set the absolute orientation, sim.handle_parent to set the orientation relative to the object's parent, or an object handle relative to whose reference frame the orientation is specified. If this handle is the handle of a joint, then the quaternion is applied relative to the joint's moving frame (unless

        """
        ...

    def setObjectSel(self, objectHandles: list) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetObjectSel.htm Sets the
        object selection state

        Args:
            objectHandles (list): handles of objects to be selected

        """
        ...

    def setPage(self, index: int) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetPage.htm Switches
        between pages (main scene views)

        Args:
            index (int): index of the page. Valid values are 0-7

        """
        ...

    def setPointCloudOptions(
        self,
        pcHandle: int,
        maxVoxelSize: float,
        maxPtCntPerVoxel: int,
        options: int,
        pointSize: float,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetPointCloudOptions.htm
        Sets various properties of a  point cloud

        Args:
            pcHandle (int): handle of the point cloud
            maxVoxelSize (float): maximum size of the OC tree voxels containing points
            maxPtCntPerVoxel (int): maximum number of points allowed in a same OC tree voxel
            options (int): bit-coded:
            pointSize (float): size of the points, in pixels

        """
        ...

    def setPoseProperty(
        self,
        target: int,
        propertyName: str,
        propertyState: list,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetPoseProperty.htm Sets
        a pose property (double[7]: x, y, z, qx, qy, qz, qw)

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (list): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setProperties(self, target: int, properties: dict) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetProperties.htm
        Convenience function to set several properties at once

        Args:
            target (int): target item
            properties (dict): a map where keys are propertyNames and values are propertyStates

        """
        ...

    def setProperty(
        self,
        target: int,
        propertyName: str,
        propertyState: Any,
        propertyType: int,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetProperty.htm
        Convenience function to set a property

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (any): property value
            propertyType (int): an optional property type

        """
        ...

    def setQuaternionProperty(
        self,
        target: int,
        propertyName: str,
        propertyState: list,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetQuaternionProperty.htm
        Sets a quaternion property (double[4]: qx, qy, qz, qw)

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (list): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setReferencedHandles(
        self, objectHandle: int, referencedHandles: list, tag: str
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetReferencedHandles.htm
        Attaches a list of custom handles to a given scene object. Those custom
        handles are handles of other scene objects, that are linked to the given
        scene object (for whatever purpose). The advantage of storing references to
        other objects with this function is that CoppeliaSim will take care of
        correctly adjusting the references if needed: For instance, imagine  objectA
        storing the handle of  objectB  via this function. If  objectB  is deleted,
        then the stored handle becomes -1. If  objectA  and  objectB  are duplicated
        at the same time, then the duplicate of  objectA  stores the handle of the
        duplicate of  objectB . Optionally, if sim.handleflag_keeporiginal  is
        specified, then linking to original objects is guaranteed, e.g. in above
        example, after a duplication of  objectA , the duplicate of  objectA  will
        store the handle of the original  objectB  (if  objectB  still exists)

        Args:
            objectHandle (int): handle of the scene object that will store the list of handles. Can be optionally combined with
            referencedHandles (list): list of scene object handles.
            tag (str): a tag: handles will be stored under this tag. Defaults to an empty tag

        """
        ...

    def setShapeBB(self, shapeHandle: int, size: list) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetShapeBB.htm Sets the
        size of a shape's bounding box, effectively scaling the shape. Non-isometric
        scaling is not always possible

        Args:
            shapeHandle (int): handle of the shape
            size (list): size of the bounding box

        """
        ...

    def setShapeColor(
        self,
        shapeHandle: int,
        colorName: str,
        colorComponent: int,
        rgbData: list,
    ) -> None:
        """
            URL: https://manual.coppeliarobotics.com/en/sim/simSetShapeColor.htm Sets
            the color of a shape

            Args:
                shapeHandle (int): handle of the shape
                colorName (str): name of a color. Can be an empty str, but if a name is provided, only shapes (or sub-entities of them) with a same color name will be modified. If colorName is
        @compound
        , then all individual colors of a compound shape can be set at once
                colorComponent (int): color component
                rgbData (list): red, green and blue components of the color (3 values), or the transparency value (1 value)

        """
        ...

    def setShapeInertia(
        self, shapeHandle: int, inertiaMatrix: list, transformationMatrix: list
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetShapeInertia.htm
        Applies a new inertia matrix to a shape. If simulation is running, the shape
        is dynamically reset (similar to calling  sim.resetDynamicObject  right
        after)

        Args:
            shapeHandle (int): handle of the
            inertiaMatrix (list): new inertia matrix (9 values), expressed relative to
            transformationMatrix (list): a transformation matrix (array of 12 values [Vx0 Vy0 Vz0 P0 Vx1 Vy1 Vz1 P1 Vx2 Vy2 Vz2 P2]) expressed relative to the shape's reference frame. The matrix indicates the center of mass of the shape, and is the frame relative to which

        """
        ...

    def setShapeMass(self, shapeHandle: int, mass: float) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetShapeMass.htm Applies
        a new mass value to a shape. If simulation is running, the shape is
        dynamically reset (similar to calling  sim.resetDynamicObject  right after)

        Args:
            shapeHandle (int): handle of the
            mass (float): new mass of the shape

        """
        ...

    def setShapeTexture(
        self,
        shapeHandle: int,
        textureId: int,
        mappingMode: int,
        options: int,
        uvScaling: list,
        position: list,
        orientation: list,
    ) -> None:
        """
            URL: https://manual.coppeliarobotics.com/en/sim/simSetShapeTexture.htm
            Applies/removes a texture to/from a shape

            Args:
                shapeHandle (int): handle of the shape.
                textureId (int): ID of the texture or -1 to remove any existing texture. See also
                mappingMode (int): texture mapping mode
        .
                options (int): bit-coded:
                uvScaling (list): array of 2 values indicating the texture scaling factors along the U and V directions
                position (list): array of 3 values x/y/z indicating the texture position on the shape. Can be None/nil for default values
                orientation (list): array of 3 values (Euler angles) indicating the texture orientation on the shape. Can be None/nil for default values

        """
        ...

    def setStepping(self, enable: bool) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetStepping.htm Enables
        or disables the stepping operation mode for a threaded script. If enabled,
        then the current script has to trigger each simulation step explicitly, via
        sim.step . Is applied cumulatively, i.e. if the stepping operation mode is
        enabled n times, it needs to be disabled n times to return to the initial
        state (Lua specific: in stepping operation mode, automatic thread
        interruptions, i.e. preemptive threading, is supressed)

        Args:
            enable (bool): enable state of thread interruption

        Returns:
            prevStepLevel (int): previous level of thread interruption. When 0, thread interruption was not enabled previously

        """
        ...

    def setstrProperty(
        self, target: int, propertyName: str, propertyState: str, options: dict
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetstrProperty.htm
        Sets a str property (text)

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (str): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setVector2Property(
        self,
        target: int,
        propertyName: str,
        propertyState: list,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetVector2Property.htm
        Sets a vector2 property (double[2])

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (list): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setVector3Property(
        self,
        target: int,
        propertyName: str,
        propertyState: list,
        options: dict,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetVector3Property.htm
        Sets a vector3 property (double[3])

        Args:
            target (int): target item
            propertyName (str): property name
            propertyState (list): property value
            options (dict): an optional map. Set options.noError to true for silent errors

        """
        ...

    def setVisionSensorImg(
        self,
        sensorHandle: int,
        image: bytes,
        options: int,
        pos: list[int] = [0, 0],
        size: list[int] = [0, 0],
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSetVisionSensorImg.htm
        Writes the image of a vision sensor (and applies any image processing via
        the vision callback functions ). Make sure the vision sensor is flagged as
        external input

        Args:
            sensorHandle (int): handle of the vision sensor object
            image (bytes): buffer containing the image
            options (int): options, bit-coded:
            pos (list): position of the image portion to write, defaults to [0 0]
            size (list): size of the image portion to write, defaults to [0 0], which corresponds to [resolutionX resolutionY]

        """
        ...

    def startSimulation(self) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simStartSimulation.htm
        Requests a start of a simulation (or a resume of a paused simulation)

        """
        ...

    def step(self) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simStep.htm Triggers the
        next simulation step, when in stepping operation mode. When simulation is
        running, then sim.step only returns once the simulation time has changed

        """
        ...

    def stopSimulation(self, wait: bool) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simStopSimulation.htm
        Requests a stop of the running simulation

        Args:
            wait (bool): if true, will wait until the simulation state is sim.simulation_stopped, otherwise only triggers a stop request. If true, calling script cannot be the main- or a simulation script, and should run threaded.

        """
        ...

    def subtractObjectFromOctree(
        self, octreeHandle: int, objectHandle: int, options: int
    ) -> int:
        """
        URL:
        https://manual.coppeliarobotics.com/en/sim/simSubtractObjectFromOctree.htm
        Removes an object from an  OC tree , as voxel subtractions

        Args:
            octreeHandle (int): handle of the OC tree
            objectHandle (int): handle of the object to subtract. Only potentially
            options (int): reserved. Set to 0

        Returns:
            totalVoxelCnt (int): total number of voxels in the OC tree

        """
        ...

    def subtractObjectFromPointCloud(
        self, pcHandle: int, objectHandle: int, options: int, tolerance: float
    ) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSubtractObjectFromPointCl
        oud.htm Removes an object from a  point cloud , as a subtraction

        Args:
            pcHandle (int): handle of the point cloud
            objectHandle (int): handle of the object to subtract. Only potentially
            options (int): reserved. Set to 0
            tolerance (float): distance used as a tolerance value

        Returns:
            totalPointCnt (int): total number of points in the point cloud

        """
        ...

    def systemSemaphore(self, key: str, acquire: bool) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simSystemSemaphore.htm
        Acquires or releases a system-wide semaphore, i.e. across several
        CoppeliaSim instances

        Args:
            key (str): the key
            acquire (bool): whether the semaphore should be acquired or released

        """
        ...

    def textEditorClose(self, handle: int) -> Tuple[str, list, list]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simTextEditorClose.htm
        Closes a text edition window previously opened with  sim.textEditorOpen

        Args:
            handle (int): handle of the text editor window

        Returns:
            text (str): text of the editor
            pos (list): size of the editor
            size (list): Description not provided

        """
        ...

    def textEditorGetInfo(self, handle: int) -> Tuple[str, list, list, bool]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simTextEditorGetInfo.htm
        Retieves information from a text edition window previously opened with
        sim.textEditorOpen

        Args:
            handle (int): handle of the text editor window

        Returns:
            text (str): text of the editor, or None/nil if the given handle is not associated with any text editor window (or the window was already closed)
            pos (list): size of the editor
            size (list): absolute position the editor
            visible (bool): Description not provided

        """
        ...

    def textEditorOpen(self, initText: str, properties: str) -> int:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simTextEditorOpen.htm Opens
        a text edition window

        Args:
            initText (str): initial text to be displayed.
            properties (str): Description not provided

        Returns:
            handle (int): handle of the text editor

        """
        ...

    def textEditorShow(self, handle: int, showState: bool) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simTextEditorShow.htm Shows
        or hides a text edition window previously opened with  sim.textEditorOpen

        Args:
            handle (int): handle of the text editor window
            showState (bool): desired show state of the text editor window

        """
        ...

    def transformBuffer(
        self,
        inBuff: bytes,
        inFormat: int,
        mult: float,
        off: float,
        outFormat: int,
    ) -> Any:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simTransformBuffer.htm
        Modifies a buffer than contains packed data

        Args:
            inBuff (bytes): input buffer that contains packed data
            inFormat (int): buffer type
            mult (float): multiplier value. We have out = offset + multiplier * in
            off (float): Description not provided
            outFormat (int): desired

        Returns:
            a) bytes outBuff (Any): No detailed return description.

        """
        ...

    def transformImage(
        self, image: bytes, resolution: list, options: int
    ) -> bytes:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simTransformImage.htm
        Transforms an image in various ways

        Args:
            image (bytes): buffer to rgb or rgba values of the image. Beware that in Lua, this image buffer will be modified!
            resolution (list): resolution of the image
            options (int): bit-coded:

        Returns:
            newImage (bytes): buffer of the transformed image

        """
        ...

    def ungroupShape(self, shapeHandle: int) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simUngroupShape.htm Ungroups
        a compound shape into several  shapes

        Args:
            shapeHandle (int): handles of the shape you wish to ungroup. If you specify for this argument (-2-handleOfShape), then the shape will be divided instead of ungrouped

        Returns:
            shapeHandles (list): array holding the handles of the resulting shapes

        """
        ...

    def unpackDoubleTable(
        self,
        data: bytes,
        startDoubleIndex: int,
        doubleCount: int,
        additionalByteOffset: int,
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simUnpackDoubleTable.htm
        Unpacks a str (or part of it) into an array of double floating-point
        numbers

        Args:
            data (bytes): str (values between 0 and 255) that contains packed floating-point numbers
            startDoubleIndex (int): zero-based index from which on data should be unpacked (from data[8*startDoubleIndex+1+additionalByteOffset]). Can be omitted in which case 0 is used
            doubleCount (int): amount of doubles that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of doubles should be unpacked from the indicated startIndex)
            additionalByteOffset (int): byte offset that will be added before reading the doubless. Can be omitted, in which case 0 is used.

        Returns:
            doubleNumbers (list): array containing unpacked double floating-point numbers

        """
        ...

    def unpackFloatTable(
        self,
        data: bytes,
        startFloatIndex: int,
        floatCount: int,
        additionalByteOffset: int,
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simUnpackFloatTable.htm
        Unpacks a str (or part of it) into an array of floating-point numbers

        Args:
            data (bytes): str (values between 0 and 255) that contains packed floating-point numbers
            startFloatIndex (int): zero-based index from which on data should be unpacked (from data[4*startFloatIndex+1+additionalByteOffset]). Can be omitted in which case 0 is used
            floatCount (int): amount of floats that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of floats should be unpacked from the indicated startFloatIndex)
            additionalByteOffset (int): byte offset that will be added before reading the floats. Can be omitted, in which case 0 is used.

        Returns:
            floatingNumbers (list): array containing unpacked floating-point numbers

        """
        ...

    def unpackInt32Table(
        self,
        data: bytes,
        startInt32Index: int,
        int32Count: int,
        additionalByteOffset: int,
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simUnpackInt32Table.htm
        Unpacks a str (or part of it) into an array of int32 numbers

        Args:
            data (bytes): str (values between 0 and 255) that contains packed int32 numbers
            startInt32Index (int): zero-based index from which on data should be unpacked (from data[4*startInt32Index+1+additionalByteOffset]). Can be omitted in which case 0 is used
            int32Count (int): amount of int32s that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of int32s should be unpacked from the indicated startInt32Index)
            additionalByteOffset (int): byte offset that will be added before reading the int32s. Can be omitted, in which case 0 is used.

        Returns:
            int32Numbers (list): array containing unpacked int32 numbers

        """
        ...

    def unpackTable(self, buffer: bytes) -> Any:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simUnpackTable.htm Unpacks a
        buffer into a table

        Args:
            buffer (bytes): an input buffer

        Returns:
            list/dict aTable (Any): No detailed return description.

        """
        ...

    def unpackUInt16Table(
        self,
        data: bytes,
        starUint16Index: int,
        uint16Count: int,
        additionalByteOffset: int,
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simUnpackUInt16Table.htm
        Unpacks a str (or part of it) into an array of uint16 numbers

        Args:
            data (bytes): str (values between 0 and 255) that contains packed uint16 numbers
            starUint16Index (int): zero-based index from which on data should be unpacked (from data[2*starUint16Index+1+additionalByteOffset]). Can be omitted in which case 0 is used.
            uint16Count (int): amount of uint16s that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of uint16s should be unpacked from the indicated starUint16Index).
            additionalByteOffset (int): byte offset that will be added before reading the uint16s. Can be omitted, in which case 0 is used.

        Returns:
            uint16Numbers (list): array containing unpacked uint16 numbers

        """
        ...

    def unpackUInt32Table(
        self,
        data: bytes,
        startUint32Index: int,
        uint32Count: int,
        additionalByteOffset: int,
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simUnpackUInt32Table.htm
        Unpacks a str (or part of it) into an array of uint32 numbers

        Args:
            data (bytes): str (values between 0 and 255) that contains packed uint32 numbers
            startUint32Index (int): zero-based index from which on data should be unpacked (from data[4*startUint32Index+1+additionalByteOffset]). Can be omitted in which case 0 is used
            uint32Count (int): amount of uint32s that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of uint32s should be unpacked from the indicated startUint32Index)
            additionalByteOffset (int): byte offset that will be added before reading the uint32s. Can be omitted, in which case 0 is used.

        Returns:
            uint32Numbers (list): No detailed return description.

        """
        ...

    def unpackUInt8Table(
        self, data: bytes, startUint8Index: int, uint8Count: int
    ) -> list:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simUnpackUInt8Table.htm
        Unpacks a str (or part of it) into an array of uint8 numbers

        Args:
            data (bytes): str (values between 0 and 255) that contains uint8 numbers
            startUint8Index (int): zero-based index from which on data should be unpacked (from data[startUint8Index]). Can be omitted in which case 0 is used.
            uint8Count (int): amount of uint8s that should be unpacked. Can be omitted in which case 0 is used (which indicates that the maximum of uint8s should be unpacked from the indicated startUint8Index).

        Returns:
            uint8Numbers (list): array containing uint8 numbers

        """
        ...

    def wait(self, deltaTime: float, simulationTime: bool) -> float:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simWait.htm Waits for a
        certain amount of time

        Args:
            deltaTime (float): minimum time duration to wait
            simulationTime (bool): indicates whether we want to wait in terms of simulation- or real-time

        Returns:
            deltaTimeLeft (float): "wait resolution" of this function is the simulation time step, and the sim.wait command may overshoot the requested waiting time. deltaTimeLeft is the negative overshoot time. If the function was called at simulation time X, and the function returned at simulation time Y, then deltaTimeLeft is deltaTime-(Y-X). deltaTimeLeft is also memorized internally on a thread-basis and used as compensation or correction factor in subsequent blocking commands. deltaTimeLeft is 0 if the simulationTime argument was false

        """
        ...

    def writeTexture(
        self,
        textureId: int,
        options: int,
        textureData: bytes,
        posX: int,
        posY: int,
        sizeX: int,
        sizeY: int,
        interpolation: float,
    ) -> None:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simWriteTexture.htm
        Overwrites a specific texture (or a portion of it) with RGB data

        Args:
            textureId (int): ID of the texture. See also
            options (int): bit-coded:
            textureData (bytes): RGB data to write onto the texture. Each pixel is represented with 3 bytes (0-255)
            posX (int): Description not provided
            posY (int): x/y position where to copy the RGB data. Set to 0/0 to overwrite the full texture
            sizeX (int): Description not provided
            sizeY (int): x/y size of the RGB data. Set to 0/0 to overwrite the full texture
            interpolation (float): fade or interpolation factor. 0 for no fade

        """
        ...

    def yawPitchRollToAlphaBetaGamma(
        self, yaw: float, pitch: float, roll: float
    ) -> Tuple[float, float, float]:
        """
        URL: https://manual.coppeliarobotics.com/en/sim/simYawPitchRollToAlphaBetaGa
        mma.htm Converts Yaw-Pitch-Roll angles to CoppeliaSim's alpha-beta-gamma
        angles

        Args:
            yaw (float): the yaw angle
            pitch (float): the pitch angle
            roll (float): the roll angle

        Returns:
            alpha (float): the alpha angle
            beta (float): the beta angle
            gamma (float): the gamma angle

        """
        ...
