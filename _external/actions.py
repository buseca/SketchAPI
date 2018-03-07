#!/usr/bin/env python

import os

actions = [
    "AddAsLibrary",
    "AddBorder",
    "AddExportFormat",
    "AddFill",
    "AddFlow",
    "AddFlowBack",
    "AddFlowHome",
    "AddInnerShadow",
    "AddShadow",
    "AlignBottom",
    "AlignCenter",
    "AlignJustified",
    "AlignLayersBottom",
    "AlignLayersCenter",
    "AlignLayersLeft",
    "AlignLayersMiddle",
    "AlignLayersRight",
    "AlignLayersTop",
    "AlignLeft",
    "AlignMiddle",
    "AlignRight",
    "AlignTop",
    "AlignmentActions",
    "ApplyFlip",
    "ApplySharedLayerStyle",
    "ApplySharedTextStyle",
    "AssignColorSpace",
    "AutoExpandGroups",
    "BackToInstance",
    "BadgeMenu",
    "BadgeMenu",
    "BaseAlignLayers",
    "BaseStyle",
    "BooleanMenu",
    "BooleanTouchBarGroup",
    "CenterLayersInCanvas",
    "CenterSelectionInVisibleArea",
    "ChangeFlowAnimationFromBottomAnimation",
    "ChangeFlowAnimationFromLeftAnimation",
    "ChangeFlowAnimationFromRightAnimation",
    "ChangeFlowAnimationFromTopAnimation",
    "ChangeFlowAnimationNoAnimation",
    "ChangeFont",
    "ClippingMask",
    "ClippingMaskMode",
    "ClosePath",
    "Cloud",
    "CollapseAllGroups",
    "ColorInspectorCircularGradientTab",
    "ColorInspectorColorTab",
    "ColorInspectorImageTab",
    "ColorInspectorLinearGradientTab",
    "ColorInspectorModeBorderTouchBarGroup",
    "ColorInspectorModeFillTouchBarGroup",
    "ColorInspectorModePicker",
    "ColorInspectorRadialGradientTab",
    "ConstraintFixHeight",
    "ConstraintFixWidth",
    "ConstraintPinBottom",
    "ConstraintPinLeft",
    "ConstraintPinRight",
    "ConstraintPinTop",
    "ConstraintReset",
    "ConvertColorSpace",
    "ConvertFlowToHotspot",
    "ConvertSymbolOrDetachInstances",
    "ConvertToOutlines",
    "Copy",
    "CopyCSSAttributes",
    "CopySVGCode",
    "CopyStyle",
    "CreateSharedStyle",
    "CreateSymbol",
    "CurveModeAsymmetric",
    "CurveModeDisconnected",
    "CurveModeMirrored",
    "CurveModeStraight",
    "CurveModeTouchGroup",
    "Cut",
    "Data",
    "DefaultStyle",
    "Delete",
    "DetachSharedStyle",
    "Difference",
    "DistributeActions",
    "DistributeHorizontally",
    "DistributeVertically",
    "Duplicate",
    "Edit",
    "EditColorSpace",
    "Export",
    "ExportPDFBook",
    "ExportSelectionWithExportFormats",
    "FindLayer",
    "Flatten",
    "FlattenSelection",
    "FlipHorizontal",
    "FlipVertical",
    "FollowFlow",
    "GridSettings",
    "Group",
    "HideAllGridsAndLayouts",
    "HideLayer",
    "IgnoreClippingMask",
    "ImageOriginalSize",
    "IncompatiblePluginsDisabled",
    "InsertArrow",
    "InsertArtboard",
    "InsertHotspot",
    "InsertImage",
    "InsertLine",
    "InsertMenu",
    "InsertSharedText",
    "InsertSlice",
    "InsertSymbol",
    "InsertTextLayer",
    "InsertVector",
    "Intersect",
    "Join",
    "LayerFocusActions",
    "LayerHeightFocus",
    "LayerWidthFocus",
    "LayerXFocus",
    "LayerYFocus",
    "LayoutSettings",
    "LicenseExpired",
    "LockLayer",
    "Magnifier",
    "MakeGrid",
    "MakeLowercase",
    "MakeUppercase",
    "ManageForeignSymbol",
    "ManageLayerStyles",
    "ManageTextStyles",
    "MaskWithShape",
    "Mirror",
    "MoveBackward",
    "MoveForward",
    "MoveToBack",
    "MoveToFront",
    "MoveToTop",
    "MoveUpHierarchy",
    "NewPage",
    "NextPage",
    "OpenPreview",
    "OpenStyleInLibrary",
    "OpenSymbolInLibrary",
    "OvalShape",
    "Paste",
    "PasteHere",
    "PasteOverSelection",
    "PasteStyle",
    "Pencil",
    "PolygonShape",
    "PreviewAtActualSize",
    "PreviousPage",
    "Print",
    "RectangleShape",
    "Redo",
    "ReduceFileSize",
    "ReduceImageSize",
    "RemoveFlow",
    "RemoveTextTransform",
    "RemoveUnusedStyles",
    "RenameLayer",
    "ReplaceColor",
    "ReplaceFonts",
    "ReplaceImage",
    "ReplaceWithSymbol",
    "ResetBoolean",
    "ResetSharedStyle",
    "ResetSymbolSize",
    "ResizeArtboardToFit",
    "RevealInLayerList",
    "ReversePath",
    "Rotate",
    "RotateClockwise",
    "RotateCounterclockwise",
    "RoundToPixel",
    "RoundedRectangleShape",
    "SaveAsTemplate",
    "Scale",
    "Scissors",
    "SelectAll",
    "SelectAllArtboards",
    "SendToSymbolsPage",
    "Shape",
    "ShowBorderOptions",
    "ShowFillOptions",
    "ShowReplaceColorSheet",
    "SmartRotate",
    "SpiralShape",
    "Split",
    "StarShape",
    "Subtract",
    "SyncLibrary",
    "SyncSharedStyle",
    "TextAlignTouchBarGroup",
    "TextOnPath",
    "TextStyleTouchBar",
    "ToggleAlignmentGuides",
    "ToggleArtboardShadow",
    "ToggleBorder",
    "ToggleFill",
    "ToggleFlowInteraction",
    "ToggleGrid",
    "ToggleInspectorVisibility",
    "ToggleInterface",
    "ToggleLayerHighlight",
    "ToggleLayerListVisibility",
    "ToggleLayout",
    "TogglePixelGrid",
    "TogglePixelLines",
    "ToggleRulers",
    "ToggleSelection",
    "ToggleSliceInteraction",
    "ToggleToolbarVisibility",
    "ToolsMenu",
    "Transform",
    "TriangleShape",
    "Underline",
    "Undo",
    "Ungroup",
    "Union",
    "UnlinkAndSyncSharedStyle",
    "UnlinkSharedStyle",
    "UpdatePlugins",
    "ViewMenu",
    "Zoom",
    "ZoomActions",
    "ZoomIn",
    "ZoomOut",
    "ZoomToActualSize",
    "ZoomToArtboard",
    "ZoomToSelection"
]

fakeActions = [
    "ArtboardChanged",
    "CloseDocument",
    "DocumentSaved",
    "ExportSlices",
    "HandlerGotFocus",
    "HandlerLostFocus",
    "HandleURL",
    "LayersMoved",
    "OpenDocument",
    "RunPluginCommand",
    "SelectionChanged",
    "TextChanged"
]

allActions = actions + fakeActions

actionsPath = "_actions"
if not os.path.exists(actionsPath):
    os.mkdir(actionsPath)

for action in allActions:
    with open(os.path.join(actionsPath, action +".md"), "w") as f:
        stub = "---\ntitle: {0}\nsummary: work in progress\n---\n\nWork In Progress\n\nDocumentation for the {0} action will appear here.".format(action)
        f.write(stub)
