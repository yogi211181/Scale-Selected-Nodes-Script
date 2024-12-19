import nuke

def scale_selected_nodes():
    """
    Scales the selected nodes by adjusting their positions relative to the center
    of the selection. Left-click dragging adjusts their spread.
    """
    # Get selected nodes
    selected_nodes = nuke.selectedNodes()
    if not selected_nodes:
        nuke.message("No nodes selected. Please select nodes to scale.")
        return

    # Calculate the center of the selected nodes
    x_positions = [node.xpos() for node in selected_nodes]
    y_positions = [node.ypos() for node in selected_nodes]
    center_x = sum(x_positions) / len(x_positions)
    center_y = sum(y_positions) / len(y_positions)

    # Prompt for scaling factor
    try:
        scaling_factor = float(nuke.getInput("Enter scaling factor (e.g., 1.5 to scale up, 0.5 to scale down):", "1.0"))
    except (TypeError, ValueError):
        nuke.message("Invalid input. Scaling factor must be a number.")
        return

    # Apply scaling
    for node in selected_nodes:
        # Calculate the new positions relative to the center
        new_x = center_x + (node.xpos() - center_x) * scaling_factor
        new_y = center_y + (node.ypos() - center_y) * scaling_factor

        # Update node position
        node.setXpos(int(new_x))
        node.setYpos(int(new_y))

    nuke.message("Nodes scaled successfully.")

# Register the function in the menu with a shortcut
nuke.menu('Nuke').addCommand("Edit/Scale Selected Nodes", scale_selected_nodes, "Ctrl+Shift+S")
