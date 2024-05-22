package async

var logCounts map[string]uint64

func Log(id, str string) {

	_, ok := logCounts[id]

}
