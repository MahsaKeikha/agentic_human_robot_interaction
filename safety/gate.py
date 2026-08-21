def authorize(action):
    blocked={"robot_command","actuate","coerce_user","hide_uncertainty"}
    return {"allowed":action not in blocked,"reason":"outside responsible HRI scope" if action in blocked else "reviewable"}
