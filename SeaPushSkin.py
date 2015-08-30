# v1.1.4 for Live 9.1.4 - Modified by Stray on 7/29/2014
# The color scheme was choosen by Ableton forum user triant (https://github.com/mrk/seapush). 
        
from Colors import Basic, Rgb, Pulse, Blink, BiLed

class Colors:

    class Option:
        Selected = BiLed.AMBER
        Unselected = BiLed.YELLOW_HALF
        On = BiLed.YELLOW
        Off = BiLed.OFF
        Unused = BiLed.OFF

    class List:
        ScrollerOn = BiLed.AMBER
        ScrollerOff = BiLed.AMBER_HALF

    class DefaultButton:
        On = Basic.FULL
        Off = Basic.HALF
        Disabled = Basic.OFF
        Alert = Basic.FULL_BLINK_SLOW

    class DefaultMatrix:
        On = Rgb.WHITE
        Off = Rgb.BLACK

    class Scales:
        Selected = BiLed.YELLOW
        Unselected = BiLed.GREEN_HALF
        FixedOn = BiLed.AMBER
        FixedOff = BiLed.YELLOW_HALF
        Diatonic = BiLed.AMBER
        Chromatic = BiLed.YELLOW_HALF

    class Instrument:
        NoteBase = Rgb.ORCHID
        NoteScale = Rgb.TURQUOISE.shade(1)
        NoteNotScale = Rgb.BLACK
        NoteInvalid = Rgb.BLACK
        Feedback = Rgb.LIME
        FeedbackRecord = Rgb.RED.shade(1)
        NoteAction = Rgb.RED

    class Recording:
        On = Basic.FULL
        Off = Basic.HALF
        Transition = Basic.FULL_BLINK_FAST

    class Session:
        Scene = BiLed.GREEN
        SceneTriggered = BiLed.GREEN_BLINK_FAST
        NoScene = BiLed.OFF
        ClipStopped = Rgb.AMBER
        ClipStarted = Pulse(Rgb.GREEN.shade(1), Rgb.GREEN, 48)
        ClipRecording = Pulse(Rgb.BLACK, Rgb.RED, 48)
        ClipTriggeredPlay = Blink(Rgb.GREEN, Rgb.BLACK, 24)
        ClipTriggeredRecord = Blink(Rgb.RED, Rgb.BLACK, 24)
        ClipEmpty = Rgb.BLACK
        RecordButton = Rgb.RED.shade(2)
        StopClip = Rgb.RED
        StopClipTriggered = Blink(Rgb.RED, Rgb.BLACK, 24)
        StoppedClip = Rgb.DARK_GREY

    class Zooming:
        Selected = Rgb.AMBER
        Stopped = Rgb.RED
        Playing = Rgb.GREEN
        Empty = Rgb.BLACK

    class TrackState:
        Common = Rgb.BLACK
        Stopped = Rgb.RED
        Disabled = Basic.OFF

    class DrumGroup:
        PadSelected = Rgb.MAGENTA
        PadSelectedNotSoloed = Rgb.MAGENTA.shade(1)
        PadFilled = Rgb.ORCHID.shade(1)
        PadEmpty = Rgb.BLUE.shade(2)
        PadMuted = Rgb.YELLOW.shade(1)
        PadMutedSelected = Rgb.AMBER
        PadSoloed = Rgb.OCEAN.highlight()
        PadSoloedSelected = Rgb.OCEAN
        PadInvisible = Rgb.BLACK
        PadAction = Rgb.RED

    class LoopSelector:
        Playhead = Rgb.GREEN
        PlayheadRecord = Rgb.RED
        SelectedPage = Rgb.YELLOW.highlight()
        InsideLoopStartBar = Rgb.WHITE
        InsideLoop = Rgb.WHITE
        OutsideLoop = Rgb.BLACK

    class NoteEditor:

        class Step:
            Low = Rgb.SKY.highlight()
            High = Rgb.OCEAN
            Full = Rgb.BLUE
            Muted = Rgb.AMBER.shade(2)

        class StepEditing:
            Low = Rgb.YELLOW.highlight()
            High = Rgb.YELLOW
            Full = Rgb.AMBER
            Muted = Rgb.WHITE

        StepSelected = Rgb.WHITE
        StepEmpty = Rgb.BLACK
        StepEmptyBase = Rgb.OCEAN.shade(2)
        StepEmptyScale = Rgb.DARK_GREY
        StepDisabled = Rgb.RED.shade(2)
        Playhead = Rgb.GREEN
        PlayheadRecord = Rgb.RED
        QuantizationSelected = BiLed.GREEN
        QuantizationUnselected = BiLed.YELLOW
        NoteBase = Rgb.OCEAN.shade(2)
        NoteScale = Rgb.DARK_GREY
        NoteNotScale = Rgb.BLACK
        NoteInvalid = Rgb.RED.shade(2)

    class Melodic:
        Playhead = Rgb.GREEN.shade(1)
        PlayheadRecord = Rgb.RED.shade(1)

    class NoteRepeat:
        RateSelected = BiLed.RED
        RateUnselected = BiLed.YELLOW

    class Mixer:
        SoloOn = Rgb.BLUE
        SoloOff = Rgb.DARK_GREY
        MuteOn = Rgb.DARK_GREY
        MuteOff = BiLed.YELLOW
        ArmSelected = BiLed.RED
        ArmUnselected = BiLed.RED_HALF

    class Browser:
        Load = BiLed.GREEN
        LoadNext = BiLed.YELLOW
        LoadNotPossible = BiLed.OFF
        Loading = BiLed.OFF

    class MessageBox:
        Cancel = BiLed.GREEN
