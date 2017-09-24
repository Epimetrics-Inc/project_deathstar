import Index from '~/pages/index.vue'
import Navheader from '~/components/navheader.vue'
import Navsearch from '~/components/navsearch.vue'
import { mount, shallow } from 'avoriaz'

describe('index.vue', () => {
  it('Render navsearch and navheader', () => {
    const wrapper = shallow(Index)
    expect(wrapper.contains(Navheader)).to.equal(true)
    expect(wrapper.contains(Navsearch)).to.equal(true)
  })

  it('Zoom in', done => {
    const wrapper = mount(Index)

    expect(wrapper.find('#zoom-wrapper')[0].hasStyle('fontSize', '15px')).to.equal(true)
    wrapper.find('#zoom-in-button')[0].trigger('click')

    wrapper.vm.$nextTick().then(() => {
      expect(wrapper.find('#zoom-wrapper')[0].hasStyle('fontSize', '20px')).to.equal(true)
    }).then(done, done);
  })

  it('Zoom out', done => {
    const wrapper = mount(Index)
    expect(wrapper.find('#zoom-wrapper')[0].hasStyle('fontSize', '15px')).to.equal(true)
    wrapper.find('#zoom-out-button')[0].trigger('click')

    wrapper.vm.$nextTick().then(() => {
      expect(wrapper.find('#zoom-wrapper')[0].hasStyle('fontSize', '10px')).to.equal(true)
    }).then(done, done);
  })
})